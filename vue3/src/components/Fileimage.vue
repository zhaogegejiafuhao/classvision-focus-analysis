<template>
    <div class="component-5579_151552">
        <div id="5579_151552" class="Pixso-symbol-5579_151552">
            <div
                id="5579_151553"
                class="Pixso-symbol-5579_151553"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151554">
                    <div
                        id="5579_151554"
                        class="Pixso-vector-5579_151554"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151559"
                class="Pixso-symbol-5579_151559"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151560">
                    <div
                        id="5579_151560"
                        class="Pixso-vector-5579_151560"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151561"
                class="Pixso-symbol-5579_151561"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151562">
                    <div
                        id="5579_151562"
                        class="Pixso-vector-5579_151562"
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
.Pixso-symbol-5579_151552 {
}
.Pixso-symbol-5579_151553 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151554 {
    width: 78.12%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector319.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 15.63%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5579_151559 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151560 {
    width: 81.25%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector317.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 14.06%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5579_151561 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151562 {
    width: 78.12%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector318.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 15.63%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
