<template>
    <div class="component-5579_151763">
        <div id="5579_151763" class="Pixso-symbol-5579_151763">
            <div
                id="5579_151764"
                class="Pixso-symbol-5579_151764"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151765">
                    <div
                        id="5579_151765"
                        class="Pixso-vector-5579_151765"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151770"
                class="Pixso-symbol-5579_151770"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151771">
                    <div
                        id="5579_151771"
                        class="Pixso-vector-5579_151771"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151772"
                class="Pixso-symbol-5579_151772"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151773">
                    <div
                        id="5579_151773"
                        class="Pixso-vector-5579_151773"
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
.Pixso-symbol-5579_151763 {
}
.Pixso-symbol-5579_151764 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151765 {
    width: 75%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2065.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-symbol-5579_151770 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151771 {
    width: 78.12%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2063.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-symbol-5579_151772 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151773 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector2064.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
