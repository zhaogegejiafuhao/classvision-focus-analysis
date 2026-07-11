<template>
    <div class="component-5578_150181">
        <div id="5578_150181" class="Pixso-symbol-5578_150181">
            <div
                id="5578_150182"
                class="Pixso-symbol-5578_150182"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150183">
                    <div
                        id="5578_150183"
                        class="Pixso-vector-5578_150183"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150188"
                class="Pixso-symbol-5578_150188"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150189">
                    <div
                        id="5578_150189"
                        class="Pixso-vector-5578_150189"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150190"
                class="Pixso-symbol-5578_150190"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150191">
                    <div
                        id="5578_150191"
                        class="Pixso-vector-5578_150191"
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
.Pixso-symbol-5578_150181 {
}
.Pixso-symbol-5578_150182 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150183 {
    width: 87.5%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector77.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 15.63%;
}
.Pixso-symbol-5578_150188 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150189 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector75.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-symbol-5578_150190 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150191 {
    width: 87.5%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector76.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 15.63%;
}
</style>
