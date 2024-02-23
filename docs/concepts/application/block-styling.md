# Block Styling

When a Block is selected, it can be styled under the _'Block Styling'_  tab in the Toolbox. Styling can include changing the text color, background color, borders, typography, or dimensions of the Block. This allows you to customize the look and feel of the application based on themes or color palettes for your specific organization. You can also customize the style of certain actions such as hovering over or clicking a button, or changing the style for every second Block.

## Style Groups

A Block can also be assigned to a style group where a common set of styles can be configured and applied to multiple Blocks at the same time.

![](<../../.gitbook/assets/Style Group 1.png>)

Certain Blocks such as content cards or cards that are dragged onto the canvas already have pre-existing style groups, such as grids. These will show up under the _'Style Group'_.

![](<../../.gitbook/assets/Style Group 2.png>)

If you have a Style Group selected and make changes to any of the styling configurations, the styling will automatically be applied to all the Blocks that are also in that style group. For example, if two grids have a style group called _box-card_, and you select only one of the grids and change the background to light blue, that change will also be applied to the other grid.&#x20;

![](<../../.gitbook/assets/Style Group 3.png>)

To make changes without affecting other blocks, deselect the style group and make the changes.&#x20;

![](<../../.gitbook/assets/Style Group 4.png>)

You can add multiple style groups at a time. If a Block has multiple style groups and you only want to apply styling to one of them, make sure only that style group is selected when configuring new styles.&#x20;

![](<../../.gitbook/assets/Style Group 5.png>)

If multiple style groups are selected and the styling is changed, the styling will be applied to both of them together. For example, if you have two style groups, _box-card,_ and _lightgreen_, and you apply styling to both of them, that styling will only be applied to Blocks that have both _box-card_ and _lightgreen_ style groups.&#x20;

![](<../../.gitbook/assets/Style Group 6.png>)

## Devices

Styles can also be configured for different devices. [See the Devices article for more details on devices.](devices.md)

## Style Sections

### Dimension

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Width</td><td><a href="https://www.w3schools.com/cssref/pr_dim_width.asp"><code>width</code> sets the width of an element</a>.</td></tr><tr><td>Height</td><td><a href="https://www.w3schools.com/cssref/pr_dim_height.asp"><code>height</code> sets the height of an element</a>.</td></tr><tr><td>Min Width</td><td><a href="https://www.w3schools.com/cssref/pr_dim_min-width.asp"><code>min-width</code> defines the minimum width of an element</a>.</td></tr><tr><td>Min Height</td><td><a href="https://www.w3schools.com/cssref/pr_dim_min-height.asp"><code>min-height</code> defines the minimum height of an element</a>.</td></tr><tr><td>Max Width</td><td><a href="https://www.w3schools.com/cssref/pr_dim_max-width.asp"><code>max-width</code> defines the maximum width of an element</a>.</td></tr><tr><td>Max Height</td><td><a href="https://www.w3schools.com/cssref/pr_dim_max-height.asp"><code>max-height</code> defines the maximum height of an element</a>.</td></tr><tr><td>Margin</td><td><ul><li><a href="https://www.w3schools.com/cssref/pr_margin-top.asp"><code>margin-top</code> sets the top margin of an element.</a></li><li><a href="https://www.w3schools.com/cssref/pr_margin-right.asp"><code>margin-right</code> sets the right margin of an element.</a></li><li><a href="https://www.w3schools.com/cssref/pr_margin-bottom.asp"><code>margin-bottom</code> sets the bottom margin of an element.</a></li><li><a href="https://www.w3schools.com/cssref/pr_margin-left.asp"><code>margin-left</code> sets the left margin of an element.</a></li></ul></td></tr><tr><td>Padding</td><td><ul><li><a href="https://www.w3schools.com/cssref/pr_padding-top.asp"><code>padding-top</code> sets the top padding (space) of an element.</a></li><li><a href="https://www.w3schools.com/cssref/pr_padding-right.asp"><code>padding-right</code> sets the right padding (space) of an element.</a></li><li><a href="https://www.w3schools.com/cssref/pr_padding-bottom.asp"><code>padding-bottom</code> sets the right padding (space) of an element.</a></li><li><a href="https://www.w3schools.com/cssref/pr_padding-left.asp"><code>padding-left</code> sets the right padding (space) of an element.</a></li></ul></td></tr></tbody></table>

{% hint style="info" %}
When not using 'auto', the supported [css units](https://www.w3schools.com/cssref/css\_units.asp) for the dimension properties are:

* fixed: px
* relative: % and vh/vw
{% endhint %}

### Flex Layout

{% hint style="info" %}
Recommended reading: [Flex](flex.md) and [How to Use Flex](../../how-to-guides/apps/use-flex.md).
{% endhint %}

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Direction</td><td><a href="https://www.w3schools.com/cssref/css3_pr_flex-direction.asp"><code>flex-direction</code> specifies the direction of the flexible items</a>: Row, Row reverse, Column, or Column reverse.</td></tr><tr><td>Justify</td><td><a href="https://www.w3schools.com/cssref/css3_pr_justify-content.asp"><code>justify-content</code> aligns the flexible container's items when the items do not use all available space on the main-axis (horizontally)</a>: Start, End, Space between, Space around, or Centre.</td></tr><tr><td>Align Items</td><td><a href="https://www.w3schools.com/cssref/css3_pr_align-items.asp"><code>align-items</code> specifies the default alignment for items inside the flexible container</a>: Start, End, Bottom, Stretch, Centre.</td></tr><tr><td>Wrap</td><td><a href="https://www.w3schools.com/cssref/css3_pr_flex-wrap.asp"><code>flex-wrap</code> specifies whether the flexible items should wrap or not</a>: No wrap, Wrap, Wrap reverse.</td></tr><tr><td>Grow</td><td><a href="https://www.w3schools.com/cssref/css3_pr_flex-grow.asp"><code>flex-grow</code> is an integer that specifies how much the item will grow relative to the rest of the flexible items inside the same container.</a></td></tr><tr><td>Align Self</td><td><a href="https://www.w3schools.com/cssref/css3_pr_align-self.asp"><code>align-self</code> specifies the alignment for the selected item inside the flexible container</a>: Auto, Start, End, Bottom, Stretch, Centre.</td></tr></tbody></table>

### Typography

<table><thead><tr><th width="272">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Font</td><td><a href="https://www.w3schools.com/cssref/pr_font_font-family.asp"><code>font-family</code> specifies the font for an element</a>: Arial, Arial Black, Brush Script MT, Comic Sans MS, Courier New, Georgia, Helvetica, Impact, Lucida Sans Unicode, Tahoma, Times New Roman, Trebuchet MS, Verdana</td></tr><tr><td>Font size</td><td><a href="https://www.w3schools.com/cssref/pr_font_font-size.asp"><code>font-size</code> sets the size of a font.</a> Either string or an integer along with a fixed (px) or relative (%, em, rem, vh, or vw) <a href="https://www.w3schools.com/cssref/css_units.asp">css unit</a>.</td></tr><tr><td>Font Weight</td><td><a href="https://www.w3schools.com/cssref/pr_font_weight.asp"><code>font-weight</code> sets how thick or thin characters in text should be displayed</a>: Thin, Extra-Light, Light, Normal, Medium, Semi-Bold, Bold, Extra-Bold, or Ultra-Bold.</td></tr><tr><td>Font Style</td><td><a href="https://www.w3schools.com/cssref/pr_font_font-style.php"><code>font-style</code> specifies the font style for a text.</a> Normal, italic, or oblique.</td></tr><tr><td>Line Height</td><td><a href="https://www.w3schools.com/cssref/pr_dim_line-height.asp"><code>line-height</code> specifies the height of a line</a> using a fixed (px) or relative (%, em, rem, vw, or vh) <a href="https://www.w3schools.com/cssref/css_units.asp">css unit</a>. </td></tr><tr><td>Font Color</td><td><a href="https://www.w3schools.com/cssref/pr_text_color.asp"><code>color</code> specifies the color of text</a> by name, RGB, or RGBA.</td></tr><tr><td>Text Align</td><td><a href="https://www.w3schools.com/cssref/pr_text_text-align.asp"><code>text-align</code> specifies the horizontal alignment of text in an element</a>: Left (default), Center, Right, or Justify.</td></tr><tr><td>Text Decoration</td><td><a href="https://www.w3schools.com/cssref/pr_text_text-decoration.asp"><code>text-decoration</code> specifies the decoration added to the text</a>: Underline, Strikethrough, or None (default).</td></tr><tr><td>Word Spacing</td><td><a href="https://www.w3schools.com/cssref/pr_text_word-spacing.php"><code>word-spacing</code> increases or decreases the space in pixels between words in a text</a> (default normal). </td></tr><tr><td>Letter Spacing</td><td><p><a href="https://www.w3schools.com/cssref/pr_text_letter-spacing.asp"><code>letter-spacing</code> increases or decreases the space between characters in a text</a> (default normal). </p><p>Either string or an integer along with a fixed (px) or relative (%, em, or rem) <a href="https://www.w3schools.com/cssref/css_units.asp">css unit</a>. </p></td></tr><tr><td>Wrap Text</td><td>Sets whether text should be wrapped: Yes or No.</td></tr><tr><td>Wrap Text At</td><td>The options are Spaces, Capitals and Symbols, and Anywhere.</td></tr></tbody></table>

### Decorations

<table><thead><tr><th width="272">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Background Color</td><td><p><a href="https://www.w3schools.com/cssref/pr_background-color.asp"><code>background-color</code> sets the background color of an element</a> by name, RGB, or RGBA.</p><p>The background of an element is the total size of the element, including padding and border (but not the margin).</p></td></tr><tr><td>Border Width</td><td><ul><li><a href="https://www.w3schools.com/cssref/pr_border-top_width.asp"><code>border-top-width</code> sets the width of an element's top border</a> in px or em.</li><li><a href="https://www.w3schools.com/cssref/pr_border-right_width.asp"><code>border-right-width</code> sets the width of an element's right border</a> in px or em.</li><li><a href="https://www.w3schools.com/cssref/pr_border-bottom_width.asp"><code>border-bottom-width</code> sets the width of an element's bottom border</a> in px or em.</li><li><a href="https://www.w3schools.com/cssref/pr_border-left_width.asp"><code>border-left-width</code> sets the width of an element's left border</a> in px or em.</li></ul></td></tr><tr><td>Border Style</td><td><a href="https://www.w3schools.com/cssref/pr_border-style.asp"><code>border-style</code> sets the style of an element's four borders</a>: Solid, Dotted, Dashed, Double, Groove, Ridge, Inset, Outset, or None.</td></tr><tr><td>Border Color</td><td><a href="https://www.w3schools.com/cssref/pr_border-color.asp"><code>border-color</code> sets the color of an element's four borders</a> by name, RGB, or RGBA.</td></tr><tr><td>Border Radius</td><td><p>Add rounded borders to the corners of elements:</p><ul><li><a href="https://www.w3schools.com/cssref/css3_pr_border-top-left-radius.asp"><code>border-top-left-radius</code> defines the radius of the top-left corner.</a></li><li><a href="https://www.w3schools.com/cssref/css3_pr_border-top-right-radius.asp"><code>border-top-right-radius</code> defines the radius of the top-right corner.</a></li><li><a href="https://www.w3schools.com/cssref/css3_pr_border-bottom-left-radius.asp"><code>border-bottom-left-radius</code> defines the radius of the bottom-left corner.</a></li><li><a href="https://www.w3schools.com/cssref/css3_pr_border-bottom-right-radius.asp"><code>border-bottom-right-radius</code> defines the radius of the bottom-right corner.</a></li></ul></td></tr><tr><td>Background</td><td><p><a href="https://www.w3schools.com/cssref/css3_pr_background.asp"><code>background</code> adds one or more image layers</a>, each comprising:</p><ul><li>Image (file or URL)</li><li>Repeat (repeat, repeat-x, repeat-y, no-repeat)</li><li>Position (left top, left center, left bottom, right top, right center, right bottom, center top, center center, center bottom, </li><li>Attachment (scroll, fixed, local)</li><li>Size (auto, cover, contain)</li></ul></td></tr></tbody></table>

### Advanced Styling

These styling options are rarely needed, but they provide additional flexibility for expert users.

#### Advanced position and displayed styling

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Display</td><td><a href="https://www.w3schools.com/cssref/pr_class_display.asp"><code>display</code> specifies the type of rendering box of an element:</a> block, inline, inline-block, flex (default), or none.</td></tr><tr><td>Position</td><td><a href="https://www.w3schools.com/css/css_positioning.asp"><code>position</code> specifies the type of positioning used for an element:</a> static (default), relative, absolute, or fixed.</td></tr><tr><td>Top*</td><td><a href="https://www.w3schools.com/cssref/pr_pos_top.asp"><code>top</code> sets the vertical position of a positioned element </a> (default auto).</td></tr><tr><td>Right*</td><td><a href="https://www.w3schools.com/cssref/pr_pos_right.asp"><code>right</code> sets the horizontal position of a positioned element</a> (default auto).</td></tr><tr><td>Left*</td><td><a href="https://www.w3schools.com/cssref/pr_pos_left.asp"><code>left</code> sets the horizontal position of a positioned element</a> (default auto).</td></tr><tr><td>Bottom*</td><td><a href="https://www.w3schools.com/cssref/pr_pos_bottom.asp"><code>bottom</code> sets the vertical position of a positioned element</a> (default auto).</td></tr></tbody></table>

{% hint style="info" %}
The supported [css units](https://www.w3schools.com/cssref/css\_units.asp) for properties marked with a \* are:

* fixed: px
* relative: % and vh/vw
{% endhint %}

#### Extra advanced styling

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Transition</td><td><p><a href="https://www.w3schools.com/cssref/css3_pr_transition.asp"><code>transition</code> adds one or more transition effect layers</a>, each comprising:</p><ul><li><a href="https://www.w3schools.com/cssref/css3_pr_transition.asp"><code>transition-property</code></a> (all, width, height, background-color, transform, box-shadow, opacity)</li><li><a href="https://www.w3schools.com/cssref/css3_pr_transition-duration.php"><code>transition-duration</code></a> how many seconds the effect lasts</li><li>Easing (linear, ease, ease-in, ease-out, ease-in-out)</li></ul></td></tr><tr><td>Perspective</td><td><a href="https://www.w3schools.com/cssref/css3_pr_perspective.asp"><code>perspective</code> defines how far the object is away from the user.</a> A lower value will result in a more intensive 3D effect than a higher value.</td></tr><tr><td>Z Index</td><td><a href="https://www.w3schools.com/cssref/pr_pos_z-index.php"><code>z-index</code> specifies the stack order of a positioned element.</a></td></tr><tr><td>Transform</td><td><p><a href="https://www.w3schools.com/css/css3_3dtransforms.asp">Apply 3D mouseover effects to transformable elements</a>: </p><ul><li><code>rotateX()</code> rotates an element around its X-axis at a given degree.</li><li><code>rotateY()</code> rotates an element around its Y-axis at a given degree.</li><li><code>rotateZ()</code> rotates an element around its Z-axis at a given degree.</li><li><code>scaleX()</code> defines a 3D scale transformation by giving a value for the X-axis.</li><li><code>scaleY()</code> defines a 3D scale transformation by giving a value for the Y-axis.</li><li><code>scaleZ()</code> defines a 3D scale transformation by giving a value for the Z-axis.</li></ul></td></tr><tr><td>Pointer Events</td><td><a href="https://www.w3schools.com/cssref/css3_pr_pointer-events.asp"><code>pointer-events</code> defines whether or not an element reacts to pointer events</a>: All or None.</td></tr></tbody></table>

#### Advanced flex layout styling

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Flex Container</td><td><a href="https://www.w3schools.com/css/css3_flexbox_container.asp"><code>flex-container</code> enables all flexible items be the same length, regardless of content.</a></td></tr><tr><td>Shrink</td><td><a href="https://www.w3schools.com/cssref/css3_pr_flex-shrink.asp"><code>flex-shrink</code> is an integer that specifies how the item will shrink relative to the rest of the flexible items inside the same container.</a></td></tr><tr><td>Basis</td><td><a href="https://www.w3schools.com/cssref/css3_pr_flex-grow.asp"><code>flex-grow</code> is an integer that specifies how much the item will grow relative to the rest of the flexible items inside the same container.</a></td></tr><tr><td>Order</td><td><a href="https://www.w3schools.com/cssref/css3_pr_order.asp"><code>order</code> is an integer that specifies the order of a flexible item relative to the rest of the flexible items inside the same container.</a></td></tr></tbody></table>

#### Typography advanced styling

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Text Shadow</td><td><a href="https://www.w3schools.com/cssref/css3_pr_text-shadow.asp"><code>text-shadow</code> adds one or more layers to the text</a>, each comprising an X position, Y position, and Blur (px or %) - as well as a Color (name, RGB, or RGBA).</td></tr></tbody></table>

#### Advanced decoration styling

<table><thead><tr><th width="271">Style</th><th>CSS Property</th></tr></thead><tbody><tr><td>Overflow</td><td><a href="https://www.w3schools.com/css/css_overflow.asp"><code>overflow</code> sets the desired behavior when content does not fit in the parent element box (overflows) in the horizontal and/or vertical direction</a>: visible (default), hidden, scroll, or auto.</td></tr><tr><td>Opacity</td><td><a href="https://www.w3schools.com/cssref/css3_pr_opacity.asp"><code>opacity</code> sets the transparency of an element</a>, where 1 is not at all transparent, 0.5 is 50% see-through, and 0 is completely transparent.</td></tr><tr><td>Box Shadow</td><td><a href="https://www.w3schools.com/cssref/css3_pr_box-shadow.asp"><code>box-shadow</code> adds one or more shadow layers to an element</a>, each comprising an X position, Y position, Blur, and Spread (px or %) - as well as a Color (name, RGB, or RGBA) and Shadow Type (Outside, Inside).</td></tr></tbody></table>

## Further Reading

* [How to use Block Styling and Devices](../../how-to-guides/apps/use-block-styling-and-devices.md)
* [How to use Flex](../../how-to-guides/apps/use-flex.md)
