<template>
    <div class="component-46_273">
        <div id="46_273" class="Pixso-symbol-46_273">
            <div
                id="46_274"
                class="Pixso-symbol-46_274"
                v-if="Property1 === 'behance 1'"
            >
                <slot name="slot_46_275">
                    <div id="46_275" class="Pixso-vector-46_275"></div>
                </slot>
            </div>
            <div
                id="46_276"
                class="Pixso-symbol-46_276"
                v-if="Property1 === 'instagram-glyph-1 (1) 1'"
            >
                <slot name="slot_46_277">
                    <div id="46_277" class="Pixso-vector-46_277"></div>
                </slot>
            </div>
            <div
                id="46_278"
                class="Pixso-symbol-46_278"
                v-if="Property1 === 'linkedin-icon-1 (1) 1'"
            >
                <slot name="slot_46_279">
                    <div id="46_279" class="Pixso-vector-46_279"></div>
                </slot>
            </div>
            <div
                id="46_280"
                class="Pixso-symbol-46_280"
                v-if="Property1 === 'facebook-3-3 1'"
            >
                <slot name="slot_46_281">
                    <div id="46_281" class="Pixso-vector-46_281"></div>
                </slot>
            </div>
            <div
                id="46_282"
                class="Pixso-symbol-46_282"
                v-if="Property1 === 'dribbble-icon (1) 1'"
            >
                <slot name="slot_46_283">
                    <div id="46_283" class="Pixso-vector-46_283"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Property1: { type: String }
});
</script>
<style>
.Pixso-symbol-46_273 {
}
.Pixso-symbol-46_274 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-46_275 {
    width: 99.98%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector8.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0.02%;
    top: 16.67%;
    bottom: 20.83%;
}
.Pixso-symbol-46_276 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-46_277 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector7.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-46_278 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-46_279 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector6.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
.Pixso-symbol-46_280 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-46_281 {
    width: 50%;
    height: 108.34%;
    background-image: url(@/assets/images/Vector4.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 25%;
    right: 25%;
    top: -4.17%;
    bottom: -4.17%;
}
.Pixso-symbol-46_282 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-46_283 {
    width: 100%;
    height: 100%;
    background-image: url(@/assets/images/Vector5.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 0%;
    bottom: 0%;
}
</style>
