<template>
    <div class="component-5578_149302">
        <div id="5578_149302" class="Pixso-symbol-5578_149302">
            <div
                id="5578_149303"
                class="Pixso-symbol-5578_149303"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149304">
                    <div
                        id="5578_149304"
                        class="Pixso-vector-5578_149304"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149309"
                class="Pixso-symbol-5578_149309"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149310">
                    <div
                        id="5578_149310"
                        class="Pixso-vector-5578_149310"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149311"
                class="Pixso-symbol-5578_149311"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149312">
                    <div
                        id="5578_149312"
                        class="Pixso-vector-5578_149312"
                    ></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Format: { type: String },
    Weight: { type: String }
});
</script>
<style>
.Pixso-symbol-5578_149302 {
}
.Pixso-symbol-5578_149303 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149304 {
    width: 78.12%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector29.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 9.38%;
    top: 9.37%;
    bottom: 12.5%;
}
.Pixso-symbol-5578_149309 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149310 {
    width: 81.25%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector27.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-symbol-5578_149311 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149312 {
    width: 78.12%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector28.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 9.38%;
    top: 9.37%;
    bottom: 12.5%;
}
</style>
