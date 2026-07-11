<template>
    <div class="component-5579_152183">
        <div id="5579_152183" class="Pixso-symbol-5579_152183">
            <div
                id="5579_152184"
                class="Pixso-symbol-5579_152184"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_152185">
                    <div
                        id="5579_152185"
                        class="Pixso-vector-5579_152185"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152190"
                class="Pixso-symbol-5579_152190"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_152191">
                    <div
                        id="5579_152191"
                        class="Pixso-vector-5579_152191"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152192"
                class="Pixso-symbol-5579_152192"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_152193">
                    <div
                        id="5579_152193"
                        class="Pixso-vector-5579_152193"
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
.Pixso-symbol-5579_152183 {
}
.Pixso-symbol-5579_152184 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152185 {
    width: 56.24%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector2045.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 21.88%;
    right: 21.88%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-symbol-5579_152190 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152191 {
    width: 59.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector2043.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.31%;
    right: 20.31%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-symbol-5579_152192 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152193 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector2044.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
