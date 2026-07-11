<template>
    <div class="component-46_2">
        <div id="46_2" class="Pixso-symbol-46_2">
            <div id="2_14" class="stroke-wrapper-2_14">
                <div class="Pixso-rectangle-2_14"></div>
                <div class="stroke-2_14"></div>
            </div>
            <slot name="slot_2_15">
                <div id="2_15" class="Pixso-vector-2_15"></div>
            </slot>
            <slot name="slot_2_16">
                <p id="2_16" class="Pixso-paragraph-2_16">
                    {{ "Email Address" }}
                </p>
            </slot>
            <slot name="slot_2_17">
                <p id="2_17" class="Pixso-paragraph-2_17">
                    {{ "hakeem@digital.com" }}
                </p>
            </slot>
        </div>
    </div>
</template>
<script lang="ts" setup></script>
<style>
.Pixso-symbol-46_2 {
    width: 554px;
    height: 74px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
    mix-blend-mode: normal;
}
.Pixso-rectangle-2_14 {
    width: 100%;
    height: 100%;
    position: relative;
    background-color: rgba(255, 255, 255, 1);
    mix-blend-mode: normal;
}
.stroke-wrapper-2_14 {
    position: absolute;
    left: 0%;
    top: 0%;
    right: 0%;
    bottom: 0%;
    width: 100%;
    height: 100%;
}
.stroke-2_14 {
    position: absolute;
    inset: 0px;
    border-radius: 0px 0px 0px 0px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
    border-color: rgba(193.493088, 186.864197, 186.864197, 1);
}
.Pixso-vector-2_15 {
    width: 0.54%;
    height: 97.3%;
    background-image: url(@/assets/images/Line2.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.45%;
    right: 99.01%;
    top: 1.35%;
    bottom: 1.35%;
}
.Pixso-paragraph-2_16 {
    font-size: 18px;
    font-family: "Roboto-Regular";
    font-weight: 400;
    text-align: left;
    letter-spacing: 0em;
    text-decoration: none;
    color: rgba(0, 0, 0, 0.61);
    width: auto;
    height: auto;
    position: absolute;
    left: 4.87%;
    right: 74.19%;
    top: 16.22%;
    bottom: 55.41%;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-paragraph-2_17 {
    font-size: 18px;
    font-family: "Roboto-Medium";
    font-weight: 500;
    text-align: left;
    letter-spacing: 0em;
    text-decoration: none;
    color: rgba(55, 81, 254, 1);
    width: auto;
    height: auto;
    position: absolute;
    left: 4.87%;
    right: 64.26%;
    top: 52.7%;
    bottom: 18.92%;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
</style>
