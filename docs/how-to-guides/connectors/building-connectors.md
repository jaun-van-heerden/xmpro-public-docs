# Building Connectors

## **Overview**

To get started with developing a new Connector, create a new C# library project in Visual Studio and import the [XMPro.Integration.Framework](https://www.nuget.org/packages/XMPro.Integration.Framework) NuGet package. When writing the code for a Connector, you will have to implement one or more interfaces:

<table><thead><tr><th width="179">Interface</th><th width="128">Necessity</th><th width="388">Description</th></tr></thead><tbody><tr><td><a href="building-connectors.md#iagent">IConnector</a></td><td>Required</td><td>Provides the structure implemented by all Connectors</td></tr><tr><td><a href="building-connectors.md#iliveconnector">ILiveConnector</a></td><td>Optional</td><td>Allows the Connector to send notifications to the App Page to notify the change of entity.</td></tr><tr><td><a href="building-connectors.md#iconnectorerror">IConnectorError</a></td><td>Optional</td><td>Allows the Connector to publish error messages to the <a href="../apps/check-connector-logs.md">Connector Logs</a></td></tr></tbody></table>

## IConnector

_IConnector_ is the primary interface that must be implemented by all Connectors as it provides the structure for the workings of the Connector. There are several methods required to implement this interface.

![Fig 1: The SQL Connector Configuration](../../.gitbook/assets/Connector\_Configuration.png)

### **Settings/Configurations**

Some Connectors need to be provided with configurations by the user. For example, for a SQL Connector to get records from a SQL Database, it needs the following:

* Server Instance
* User Name
* Password
* Database

Each of these settings should be referenced in the code and must correspond to the settings template created when [packaging your Connector](packaging-agents.md).

{% hint style="info" %}
A template is a JSON representation of all the controls and their layout that will be used to capture the settings from a user.
{% endhint %}

An example of the settings template (generated using the [XMPro Package Manager](https://www.microsoft.com/en-au/p/xmpro-package-manager/9n3f4wnslgzk)) is shown in the image below. The settings in this example consist of the following controls:

* Group (Server)
* Textbox
* Checkbox
* Group (Database)
* DropDown
* ScriptBox

![Fig 2: The SQL Connector Packaging](../../.gitbook/assets/Connector\_Configuration\_Packager.png)

Each control has a _Key_, which uniquely identifies it in the template and allows the Connector code to access its value at any time. To get the value contained in a setting, use the following code:

```csharp
string mySetting = parameters[“myUniqueKey”];
```

Before a template is rendered on the screen, or if a postback occurs on any control in the template, the method below would be called to allow the Connector an opportunity to make any necessary runtime changes to the template, for example, verifying user credentials, displaying all tables of a selected database in a drop-down list, etc. In this example, no changes are being made to the template, but they can be added to the _**todo**_ section if needed.

{% hint style="info" %}
&#x20;For a postback to occur after a user navigates out of a setting field, the _Postback_ property needs to be set to _true_ when packaging the Connector.
{% endhint %}

```csharp
public string GetConfigurationTemplate(string template, IDictionary<string, string> parameters)
{

//parse settings JSON into Settings object
var settings = Settings.Parse(template);
//populate the settings/configuration controls with the user selected values
new Populator(parameters).Populate(settings);
// ToDo: update the controls, values or the data sources here
//return the updated settings xml
return settings.ToString();

}
```

### Entities

Each Connector must inform the _Engine_ about the Entities that will be produced by the Connector. To do this, implement the following method:

```csharp
public IEnumerable<Entity> GetEntities(IDictionary<string, string> parameters)
```

This method returns a collection of Entities, which represent an object or a function of the Connector. For example, an Entity can be a Table within the configured Database in the SQL Connector.

Each Entity contains the following:

<table><thead><tr><th width="285">Name</th><th>Description</th><th data-hidden></th></tr></thead><tbody><tr><td>EntityId</td><td>A unique identifier for the Entity.</td><td></td></tr><tr><td>Name</td><td>The name of the entity.</td><td></td></tr><tr><td>IsLive</td><td>Indicate if the Entity supports Live Updates.</td><td></td></tr><tr><td>Operations</td><td><p>The operations which the Entity supports.</p><ul><li><a href="building-connectors.md#read">Read</a></li><li><a href="building-connectors.md#insert">Insert</a></li><li><a href="building-connectors.md#update">Update</a></li><li><a href="building-connectors.md#undefined">Delete</a></li></ul></td><td></td></tr></tbody></table>

{% code overflow="wrap" %}
```csharp
new Entity("OpenRecommendation") { IsLive = True, Name = "Open Recommendation", Operations = Operation.Read };
```
{% endcode %}

### Entity Properties

The Connector must provide a list of the Entity's properties, which describe its key, output schema, and optional inputs. To achieve this, implement the following method:

```csharp
public Entity GetEntity(string entityId, IDictionary<string, string> parameters)
```

This method returns the Entity with a collection of properties for the selected Entity's entityId, which is passed as a parameter to this method.&#x20;

Most properties will be Output properties, which describe the Entity's data, and are indicated by setting **key** and **isParameter** to **false**. For example, this String property named _OutputString:_&#x20;

{% code overflow="wrap" %}
```csharp
new Property("OutputString", Settings.Enums.Types.String, key: false, isParameter: false) 
```
{% endcode %}

At least one property should be marked as the Entity's Key, indicated by setting **key** to **true**. The key uniquely identifies records when performing Update or Delete tasks, and for Application Blocks such as Grids that require a unique key per record. For example, this Long property named _Id:_

```csharp
new Property("Id", Settings.Enums.Types.String, key: true, isParameter: false) 
```

Finally, we have the optional Parameter properties, indicated by setting **isParameter** to **true**. They are included in the output schema, but also exposed to the App Page as optional input to the Read operation - retrieved from its _options_ parameter to modify the results. For example, this Int property named _Input_:

```csharp
new Property("Input", Settings.Enums.Types.Int, key: false, isParameter: true);
```

{% hint style="info" %}
Few Connectors need Parameter properties - they are used when the desired outcome is not achievable through the regular Configuration settings or the data source filter.

For example, the Azure Digital Twins Connector's Time Series entity includes an optional input parameter, "$ts", which shows up in the output as well as a Timestamp for that specific record/event.
{% endhint %}

### Create

The Connector must implement a method called _Create,_ which is invoked when your Connector is hosted. User-defined configuration is passed as a parameter to this method and should be stored in a class variable for later use. This is a good point to provide any resources needed for the working of your Connector.

```csharp
void Create(Configuration configuration)
{

this.config = configuration;
// ToDo: Provision any resources or write Startup logic.

}
```

### Read

The _Read_ method is one of the Entities' operations and is expected to return a JToken back to the _Engine_. This method is invoked when a Read/Refresh Action is called from a Block within an App Page.

{% code overflow="wrap" %}
```csharp
public IQueryable<JToken> Read(string entityId, OperationOptions options, out long count, JObject extraOptions = null)
```
{% endcode %}

This method contains a list of parameters being passed from the _Engine._

<table><thead><tr><th width="201">Name</th><th>Description</th><th data-hidden></th></tr></thead><tbody><tr><td>entityId</td><td>A unique identifier for the Entity</td><td></td></tr><tr><td>OperationOptions</td><td><p>The operation options as configured by a user:</p><ul><li>Parameters: a JObject containing the input parameters' value</li><li>Filter: the data filter criteria</li><li>TransactionName: the name of the transaction </li></ul></td><td></td></tr><tr><td>count</td><td>The number of records</td><td></td></tr><tr><td>extraOptions</td><td><p>A JObject contains the following:</p><ul><li>Sort: the data sorting criteria</li><li>Skip: the number of records to skip</li><li>Take: the number of records to return</li></ul></td><td></td></tr></tbody></table>

### Insert

The _Insert_ method is one of the Entities' operations and is expected to return a JObject back to the _Engine_ with the inserted record Id. This method will be invoked when an Insert Action is called from a Block within an App Page.

```csharp
public JObject Insert(string entityId, JObject values, OperationOptions options)
```

<table><thead><tr><th width="198">Name</th><th>Description</th><th data-hidden></th></tr></thead><tbody><tr><td>entityId</td><td>A unique identifier for the Entity</td><td></td></tr><tr><td>values</td><td>A JObject of values to be inserted</td><td></td></tr><tr><td>OperationOptions</td><td><p>The operation options as configured by a user:</p><ul><li>Parameters: a JObject containing the input parameters' value</li><li>Filter: the data filter criteria</li><li>TransactionName: the name of the transaction </li></ul></td><td></td></tr></tbody></table>

### Update

The _Update_ method is one of the Entities' operations and is expected to return a JObject back to the _Engine_ with the updated record Id. This method will be invoked when an Update Action is called from a Block within an App Page.

{% code overflow="wrap" %}
```csharp
public JObject Update(string entityName, JObject key, JObject values, OperationOptions options)
```
{% endcode %}

<table><thead><tr><th width="205">Name</th><th>Description</th><th data-hidden></th></tr></thead><tbody><tr><td><em>entityId</em></td><td>A unique identifier for the Entity</td><td></td></tr><tr><td>key</td><td>A JObject containing the primary key of the record to be updated</td><td></td></tr><tr><td>values</td><td>A JObject of values to be updated</td><td></td></tr><tr><td>OperationOptions</td><td><p>The operation options as configured by a user:</p><ul><li>Parameter: a JObject containing the input parameters' value</li><li>Filter: the data filter criteria.</li><li>TransactionName: the name of the transaction </li></ul></td><td></td></tr></tbody></table>

### Delete

The _Delete_ method is one of the Entities' operations and is expected to return back to the _Engine_ with the number of records deleted. This method will be invoked when a Delete Action is called from a Block within an App Page.

```csharp
public int Delete(string entityId, JObject key, OperationOptions options)
```

<table><thead><tr><th width="215">Name</th><th>Description</th><th data-hidden></th></tr></thead><tbody><tr><td>entityId</td><td>A unique identifier for the Entity</td><td></td></tr><tr><td>key</td><td>A JObject containing the primary key of the record to be deleted</td><td></td></tr><tr><td>OperationOptions</td><td><p>The operation options as configured by a user:</p><ul><li>Parameters: a JObject containing the input parameters' value</li><li>Filter: the data filter criteria</li><li>TransactionName: the name of the transaction </li></ul></td><td></td></tr></tbody></table>

### Destroy

Each Connector must implement a _Destroy_ method, which will be invoked when an App Page is closed. Use this method to release any resources or memory that your Connector may have acquired during its lifetime.

```csharp
void Destroy()
```

### Decrypting Values

If a Connector’s configuration contains a Secure/Password Textbox, its value will automatically be encrypted. To decrypt the value, use the following set of instructions:

```csharp
var request = new OnDecryptRequestArgs(value);
this.OnDecryptRequestArgs?.Invoke(this, request);
var decryptedVal = request.DecryptedValue;
```

### Custom Events

While building your Connector, you may need to use external libraries or third-party event subscriptions to handle custom events. If these are used, you must catch any exceptions from the event handlers yourself, to prevent uncaught exceptions that could possibly crash the App Page if they get through.

## ILiveConnector

The _ILiveConnector_ interface allows the Connector to send notifications to an App Page to notify of a change to the entity. There are several methods required to implement this interface.

### Subscribe

Subscribe is called by the Engine to inform the Connector that an App Page has been opened that uses Live Data from a given Entity (_IsLive property_ set to true), and should be used to begin listening for changes to that entity. The Subscribe method has two overloads and can be used in the following ways:

1. Use the first overload if you only want to pass the entity ID to the method.

```csharp
public void Subscribe(string entityId)
```

2. Use the second overload if you want to use filtering.

<pre class="language-csharp"><code class="lang-csharp"><strong>public void Subscribe(string entityId, OperationOptions options, JObject extraOptions)
</strong></code></pre>

{% hint style="warning" %}
The second overload is supported on App Designer v4.3.5 and XMPro.Integration.Framework v4.2 and above.
{% endhint %}

### UnSubscribe

Unsubscribe is called by the Engine to inform the Connector that all AppPages that use Live Data from a given Entity have been closed, and should be used to stop listening for changes to that entity.

```csharp
public void UnSubscribe(string entityId)
```

### Publish

This method can be used to allow external changes to be passed to the Connector's internal entity tracking.

```csharp
public void Publish(string entityId, Change[] changes, JObject options)
```

### OnChange

To push the changes of entities to an App Page that subscribed to the live update, your Connector should invoke the _OnChange_ event with the values of changes as arguments:

{% code overflow="wrap" %}
```csharp
this.OnChange?.Invoke(this, new OnChangeArgs() { EntityId = entityId, Changes = changes.ToArray() });
```
{% endcode %}

## IConnectorError

A Connector can publish messages to the [Connector Logs](../apps/check-connector-logs.md) by implementing the _IConnectorError_ interface.&#x20;

To log the error, your Connector should invoke the _OnConnectorError_ event with the error information passed as arguments:

{% code overflow="wrap" %}
```csharp
this.OnConnectorError?.Invoke(this, new OnErrorArgs(ConnectionId, Timestamp, Source, Error, DetailedError, Data));
```
{% endcode %}

## Example

The code below is an example of an empty connector. Take note of how the interfaces and methods have been implemented.

```csharp
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using XMPro.Integration.Framework;
using XMPro.Integration.Framework.Connector;
using XMPro.Integration.Settings;

namespace XMPro.Integration.NewConnector
{
    public class NewConnector: ILiveConnector, IUsesVariable, IConnectorError
    {
        public long UniqueId { get; set; }

        public event EventHandler<OnChangeArgs> OnChange;
        public event EventHandler<OnErrorArgs> OnConnectorError;
        public event EventHandler<OnDecryptRequestArgs> OnDecryptRequest;
        public event EventHandler<OnVariableRequestArgs> OnVariableRequest;

        private Configuration _config;
        public void Subscribe(string entityId)
        {
            // Implement script for Subscribe method
        }

        public void UnSubscribe(string entityId)
        {
            // Implement script for UnSubscribe method
        }

        public void Publish(string entityId, Change[] changes, JObject options)
        {
            // Implement script for Publish method
        }

        public string GetConfigurationTemplate(string template, IDictionary<string, string> parameters)
        {
            var settings = Settings.Settings.Parse(template);
            new Populator(parameters).Populate(settings);

            return settings.ToString();
        }

        public IEnumerable<Entity> GetEntities(IDictionary<string, string> parameters)
        {

            this._config = new Configuration(parameters);
            //Implement script for GetEntities method
            return new List<Entity>() { { new Entity("0") { Operations = Operation.Read, IsLive = false, Name = "Name" } } };

        }

        public Entity GetEntity(string entityId, IDictionary<string, string> parameters)
        {
            return new Entity(entityId)
            {
                Properties = new List<Property>().ToArray(),
                Operations = Operation.Read,
                IsLive = false
            };
        }

        public void Create(Configuration config)
        {
            //Implement script for Create method
        }

        public IQueryable<JToken> Read(string entityId, OperationOptions options, JObject extraOptions = null)
        {
            try
            {
                //Implement script for Read method
                return Enumerable.Empty<JToken>().AsQueryable();
            }
            catch (Exception e)
            {
                this.OnConnectorError?.Invoke(this, new OnErrorArgs(123, DateTime.UtcNow, nameof(Read), e.Message, e.ToString()));
                return Enumerable.Empty<JToken>().AsQueryable();
            }
        }

        public JObject Insert(string entityId, JObject values, OperationOptions options)
        {
            //Implement script for Insert method
        }

        public JObject Update(string entityId, JObject key, JObject values, OperationOptions options)
        {
            //Implement script for Update method 
        }

        public int Delete(string entityId, JObject key, OperationOptions options)
        {
            //Implement script for Delete method 
        }

        public void CommitTransaction(string transactionName)
        {
            //Implement script for CommitTransaction method 
        }

        public void Destroy()
        {
           //Implement script for Destroy method 
        }
    }
}

```

## Further Reading

* [Packaging Connectors](packaging-agents.md)
