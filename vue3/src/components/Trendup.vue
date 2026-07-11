<template>
    <div class="component-5579_151111">
        <div id="5579_151111" class="Pixso-symbol-5579_151111">
            <div
                id="5579_151112"
                class="Pixso-symbol-5579_151112"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151113">
                    <div
                        id="5579_151113"
                        class="Pixso-vector-5579_151113"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151118"
                class="Pixso-symbol-5579_151118"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151119">
                    <div
                        id="5579_151119"
                        class="Pixso-vector-5579_151119"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151120"
                class="Pixso-symbol-5579_151120"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151121">
                    <div
                        id="5579_151121"
                        class="Pixso-vector-5579_151121"
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
.Pixso-symbol-5579_151111 {
}
.Pixso-symbol-5579_151112 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151113 {
    width: 87.5%;
    height: 56.25%;
    background-image: url(@/assets/images/Vector131.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 25%;
}
.Pixso-symbol-5579_151118 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151119 {
    width: 90.63%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector129.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.68%;
    right: 4.69%;
    top: 17.19%;
    bottom: 23.43%;
}
.Pixso-symbol-5579_151120 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151121 {
    width: 87.5%;
    height: 56.25%;
    background-image: url(@/assets/images/Vector130.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 25%;
}
</style>
