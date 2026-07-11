<template>
    <div class="component-5579_152024">
        <div id="5579_152024" class="Pixso-symbol-5579_152024">
            <div
                id="5579_152025"
                class="Pixso-symbol-5579_152025"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_152026">
                    <div
                        id="5579_152026"
                        class="Pixso-vector-5579_152026"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152031"
                class="Pixso-symbol-5579_152031"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_152032">
                    <div
                        id="5579_152032"
                        class="Pixso-vector-5579_152032"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152033"
                class="Pixso-symbol-5579_152033"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_152034">
                    <div
                        id="5579_152034"
                        class="Pixso-vector-5579_152034"
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
.Pixso-symbol-5579_152024 {
}
.Pixso-symbol-5579_152025 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152026 {
    width: 87.5%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2033.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-symbol-5579_152031 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152032 {
    width: 90.62%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector2031.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-symbol-5579_152033 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152034 {
    width: 87.5%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector2032.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 18.75%;
}
</style>
