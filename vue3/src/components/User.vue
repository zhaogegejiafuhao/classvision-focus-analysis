<template>
    <div class="component-5579_152448">
        <div id="5579_152448" class="Pixso-symbol-5579_152448">
            <div
                id="5579_152449"
                class="Pixso-symbol-5579_152449"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_152450">
                    <div
                        id="5579_152450"
                        class="Pixso-vector-5579_152450"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152455"
                class="Pixso-symbol-5579_152455"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_152456">
                    <div
                        id="5579_152456"
                        class="Pixso-vector-5579_152456"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152457"
                class="Pixso-symbol-5579_152457"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_152458">
                    <div
                        id="5579_152458"
                        class="Pixso-vector-5579_152458"
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
.Pixso-symbol-5579_152448 {
}
.Pixso-symbol-5579_152449 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152450 {
    width: 81.32%;
    height: 78.21%;
    background-image: url(@/assets/images/Vector50.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.34%;
    right: 9.34%;
    top: 9.36%;
    bottom: 12.43%;
}
.Pixso-symbol-5579_152455 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152456 {
    width: 84.37%;
    height: 81.39%;
    background-image: url(@/assets/images/Vector48.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.74%;
    right: 7.89%;
    top: 7.8%;
    bottom: 10.81%;
}
.Pixso-symbol-5579_152457 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152458 {
    width: 81.24%;
    height: 78.14%;
    background-image: url(@/assets/images/Vector49.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.36%;
    bottom: 12.5%;
}
</style>
