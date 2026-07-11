<template>
    <div class="component-5579_153016">
        <div id="5579_153016" class="Pixso-symbol-5579_153016">
            <div
                id="5579_153017"
                class="Pixso-symbol-5579_153017"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_153018">
                    <div
                        id="5579_153018"
                        class="Pixso-vector-5579_153018"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153023"
                class="Pixso-symbol-5579_153023"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_153024">
                    <div
                        id="5579_153024"
                        class="Pixso-vector-5579_153024"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153025"
                class="Pixso-symbol-5579_153025"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_153026">
                    <div
                        id="5579_153026"
                        class="Pixso-vector-5579_153026"
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
.Pixso-symbol-5579_153016 {
}
.Pixso-symbol-5579_153017 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153018 {
    width: 75%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector68.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 3.13%;
    bottom: 12.5%;
}
.Pixso-symbol-5579_153023 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153024 {
    width: 78.12%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector66.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 1.56%;
    bottom: 10.94%;
}
.Pixso-symbol-5579_153025 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153026 {
    width: 75%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector67.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 3.13%;
    bottom: 12.5%;
}
</style>
