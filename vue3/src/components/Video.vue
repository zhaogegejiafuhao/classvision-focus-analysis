<template>
    <div class="component-5579_153528">
        <div id="5579_153528" class="Pixso-symbol-5579_153528">
            <div
                id="5579_153529"
                class="Pixso-symbol-5579_153529"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_153530">
                    <div
                        id="5579_153530"
                        class="Pixso-vector-5579_153530"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153535"
                class="Pixso-symbol-5579_153535"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_153536">
                    <div
                        id="5579_153536"
                        class="Pixso-vector-5579_153536"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153537"
                class="Pixso-symbol-5579_153537"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_153538">
                    <div
                        id="5579_153538"
                        class="Pixso-vector-5579_153538"
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
.Pixso-symbol-5579_153528 {
}
.Pixso-symbol-5579_153529 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153530 {
    width: 81.24%;
    height: 68.74%;
    background-image: url(@/assets/images/Vector98.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 15.63%;
    bottom: 15.63%;
}
.Pixso-symbol-5579_153535 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153536 {
    width: 84.38%;
    height: 71.88%;
    background-image: url(@/assets/images/Vector96.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 14.06%;
    bottom: 14.06%;
}
.Pixso-symbol-5579_153537 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153538 {
    width: 81.24%;
    height: 68.74%;
    background-image: url(@/assets/images/Vector97.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 15.63%;
    bottom: 15.63%;
}
</style>
