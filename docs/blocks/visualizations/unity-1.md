# Unity (Legacy)

The Unity Block can display data that is received via the Data Source and it is interactive by configuring the [Action ](../common-properties.md#action)on the Button or any other component that has that option to update the Data Source.&#x20;

{% hint style="warning" %}
This Block only supports Unity **2019** and Unity WebGL content is not currently supported on **mobile devices**.&#x20;

For newer Unity versions use the new [Unity](unity.md) Block.
{% endhint %}

{% hint style="info" %}
**Unity integration with an App**\
Use the [XMPro Integration asset on the Unity Asset Store](https://assetstore.unity.com/packages/tools/integration/xmpro-integration-179386). The asset includes a demo project and its own documentation and tutorial.
{% endhint %}

{% hint style="info" %}
**Disable Keyboard Capture**\
Is your keyboard non-responsive once a Unity model is loaded? Follow [this guide](https://docs.unity3d.com/ScriptReference/WebGLInput-captureAllKeyboardInput.html) to prevent the keyboard input from being locked to the Unity model.
{% endhint %}

![](<../../.gitbook/assets/unity pump example.gif>)

![](broken-reference)

## Model Interaction

You can interact with models that have been designed in Unity to be interacted with, by using the controls/events that the model was designed to use.

## Unity Properties

### Appearance

#### Common Properties

The _visibility_ property is common to most Blocks;

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

#### Loading Bar Image

This property gives the user an option to upload an image that will be displayed on top of the loading bar.

![](<../../.gitbook/assets/image (736).png>)

The default option is no image and just displays the loading bar.

![](<../../.gitbook/assets/image (1372).png>)

#### Loading Bar Color

This will change the color of the default bar to the selected color.

### Behavior

Here we need to configure the Unity control. All files come from the Unity build itself.&#x20;

#### Code File&#x20;

Select the Unity web assembly code file.&#x20;

The Code File property is required for the Unity Block.

#### Data File

Select the Unity data file.

The Data File property is required for the Unity Block.

#### Framework File

Select the Unity framework file.&#x20;

The Framework File property is required for the Unity Block.

{% hint style="info" %}
For more details on how to upload or manage files, [see the Manage App Files article](../../how-to-guides/apps/manage-app-files.md).
{% endhint %}

### Data Source

#### Common Properties

A Data Source is used to send data to the Unity Block. Properties that are common to most Blocks include: _filter, sort, show # of results,_ and _skip # of results;_

[See the Common Properties article for more details on common Data Source properties.](../common-properties.md#data-source)
