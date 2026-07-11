<template>
    <div class="component-21_53">
        <div id="21_53" class="stroke-wrapper-21_53">
            <div class="Pixso-symbol-21_53">
                <div id="19_37" class="Pixso-frame-19_37">
                    <slot name="slot_19_38">
                        <div id="19_38" class="Pixso-vector-19_38"></div>
                    </slot>
                </div>
                <div id="25_109" class="Pixso-frame-25_109">
                    <slot name="slot_25_110">
                        <p id="25_110" class="Pixso-paragraph-25_110">
                            {{ "Button" }}
                        </p>
                    </slot>
                </div>
                <div id="19_40" class="Pixso-frame-19_40">
                    <div class="frame-content-19_40">
                        <slot name="slot_19_41">
                            <div id="19_41" class="Pixso-vector-19_41"></div>
                        </slot>
                    </div>
                </div>
            </div>
            <div class="stroke-21_53"></div>
        </div>
    </div>
</template>
<script lang="ts" setup></script>
<style>
.Pixso-symbol-21_53 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 5px 5px 5px 5px;
    border-radius: 5px 5px 5px 5px;
    box-shadow: 0px 0px 4px 0px rgba(0, 0, 0, 0.25);
    background-color: rgba(255, 255, 255, 1);
}
.stroke-wrapper-21_53 {
    position: relative;
    width: 115px;
    height: 34px;
    display: flex;
}
.stroke-21_53 {
    position: absolute;
    inset: 0px;
    border-radius: 5px 5px 5px 5px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
    border-color: rgba(210, 226, 239, 1);
}
.Pixso-frame-19_37 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-vector-19_38 {
    width: 66.67%;
    height: 66.67%;
    background-image: url(@/assets/images/Vector4.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.83%;
    right: 12.5%;
    top: 20.83%;
    bottom: 12.5%;
}
.Pixso-frame-25_109 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 5px 5px 5px 5px;
}
.Pixso-paragraph-25_110 {
    font-size: 14px;
    font-family: "Manrope-Bold";
    font-weight: 700;
    display: flex;
    flex-direction: column;
    justify-content: center;
    letter-spacing: 0em;
    line-height: 14px;
    color: rgba(23, 26, 31, 1);
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-frame-19_40 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.frame-content-19_40 {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2px 0px 0px 0px;
    width: 100%;
    height: 100%;
    position: relative;
}
.Pixso-vector-19_41 {
    width: 9px;
    height: 6px;
    background-image: url(@/assets/images/Vector3.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
</style>
