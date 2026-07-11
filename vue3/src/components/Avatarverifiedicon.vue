<template>
    <div class="component-6168_17837">
        <div id="6168_17837" class="Pixso-symbol-6168_17837">
            <div
                id="6168_17836"
                class="Pixso-symbol-6168_17836"
                v-if="Size === 'xs'"
            >
                <slot name="slot_6168_17834">
                    <div id="6168_17834" class="Pixso-vector-6168_17834"></div>
                </slot>
                <slot name="slot_6168_17835">
                    <div id="6168_17835" class="Pixso-vector-6168_17835"></div>
                </slot>
            </div>
            <div
                id="6168_17829"
                class="Pixso-symbol-6168_17829"
                v-if="Size === 'sm'"
            >
                <slot name="slot_6168_17827">
                    <div id="6168_17827" class="Pixso-vector-6168_17827"></div>
                </slot>
                <slot name="slot_6168_17828">
                    <div id="6168_17828" class="Pixso-vector-6168_17828"></div>
                </slot>
            </div>
            <div
                id="6168_17841"
                class="Pixso-symbol-6168_17841"
                v-if="Size === 'md'"
            >
                <slot name="slot_6168_17842">
                    <div id="6168_17842" class="Pixso-vector-6168_17842"></div>
                </slot>
                <slot name="slot_6168_17843">
                    <div id="6168_17843" class="Pixso-vector-6168_17843"></div>
                </slot>
            </div>
            <div
                id="6168_17820"
                class="Pixso-symbol-6168_17820"
                v-if="Size === 'lg'"
            >
                <slot name="slot_6168_17818">
                    <div id="6168_17818" class="Pixso-vector-6168_17818"></div>
                </slot>
                <slot name="slot_6168_17819">
                    <div id="6168_17819" class="Pixso-vector-6168_17819"></div>
                </slot>
            </div>
            <div
                id="6168_17808"
                class="Pixso-symbol-6168_17808"
                v-if="Size === 'xl'"
            >
                <slot name="slot_6168_17809">
                    <div id="6168_17809" class="Pixso-vector-6168_17809"></div>
                </slot>
                <slot name="slot_6168_17810">
                    <div id="6168_17810" class="Pixso-vector-6168_17810"></div>
                </slot>
                <slot name="slot_6168_17811">
                    <div id="6168_17811" class="Pixso-vector-6168_17811"></div>
                </slot>
            </div>
            <div
                id="6168_17800"
                class="Pixso-symbol-6168_17800"
                v-if="Size === '2xl'"
            >
                <slot name="slot_6168_17802">
                    <div id="6168_17802" class="Pixso-vector-6168_17802"></div>
                </slot>
                <slot name="slot_6168_17803">
                    <div id="6168_17803" class="Pixso-vector-6168_17803"></div>
                </slot>
            </div>
            <div
                id="6168_17792"
                class="Pixso-symbol-6168_17792"
                v-if="Size === '3xl'"
            >
                <slot name="slot_6168_17794">
                    <div id="6168_17794" class="Pixso-vector-6168_17794"></div>
                </slot>
                <slot name="slot_6168_17795">
                    <div id="6168_17795" class="Pixso-vector-6168_17795"></div>
                </slot>
            </div>
            <div
                id="6168_17697"
                class="Pixso-symbol-6168_17697"
                v-if="Size === '4xl'"
            >
                <slot name="slot_6168_17687">
                    <div id="6168_17687" class="Pixso-vector-6168_17687"></div>
                </slot>
                <slot name="slot_6168_17694">
                    <div id="6168_17694" class="Pixso-vector-6168_17694"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-6168_17837 {
}
.Pixso-symbol-6168_17836 {
    width: 10px;
    height: 10px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17834 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2062.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17835 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2061.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17829 {
    width: 12px;
    height: 12px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17827 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2060.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17828 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2059.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17841 {
    width: 14px;
    height: 14px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17842 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2058.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17843 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2057.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17820 {
    width: 16px;
    height: 16px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17818 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2056.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17819 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2055.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17808 {
    width: 18px;
    height: 18px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17809 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector2054.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-vector-6168_17810 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2053.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17811 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2052.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17800 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17802 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2051.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17803 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2050.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17792 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17794 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2049.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17795 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2048.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
.Pixso-symbol-6168_17697 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6168_17687 {
    width: 87.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2047.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-vector-6168_17694 {
    width: 40.64%;
    height: 31.27%;
    background-image: url(@/assets/images/Vector2046.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.68%;
    right: 29.68%;
    top: 35.93%;
    bottom: 32.8%;
}
</style>
