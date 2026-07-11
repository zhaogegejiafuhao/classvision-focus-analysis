<template>
    <div class="component-5579_151279">
        <div id="5579_151279" class="Pixso-symbol-5579_151279">
            <div
                id="5579_151280"
                class="Pixso-symbol-5579_151280"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151281">
                    <div
                        id="5579_151281"
                        class="Pixso-vector-5579_151281"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151286"
                class="Pixso-symbol-5579_151286"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151287">
                    <div
                        id="5579_151287"
                        class="Pixso-vector-5579_151287"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151288"
                class="Pixso-symbol-5579_151288"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151289">
                    <div
                        id="5579_151289"
                        class="Pixso-vector-5579_151289"
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
.Pixso-symbol-5579_151279 {
}
.Pixso-symbol-5579_151280 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151281 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector297.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
.Pixso-symbol-5579_151286 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151287 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector295.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-symbol-5579_151288 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151289 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector296.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
