<template>
    <div class="component-5579_151720">
        <div id="5579_151720" class="Pixso-symbol-5579_151720">
            <div
                id="5579_151721"
                class="Pixso-symbol-5579_151721"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151722">
                    <div
                        id="5579_151722"
                        class="Pixso-vector-5579_151722"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151727"
                class="Pixso-symbol-5579_151727"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151728">
                    <div
                        id="5579_151728"
                        class="Pixso-vector-5579_151728"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151729"
                class="Pixso-symbol-5579_151729"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151730">
                    <div
                        id="5579_151730"
                        class="Pixso-vector-5579_151730"
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
.Pixso-symbol-5579_151720 {
}
.Pixso-symbol-5579_151721 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151722 {
    width: 75%;
    height: 56.24%;
    background-image: url(@/assets/images/Vector2030.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 21.88%;
    bottom: 21.88%;
}
.Pixso-symbol-5579_151727 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151728 {
    width: 78.12%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector2028.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-symbol-5579_151729 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151730 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector2029.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
