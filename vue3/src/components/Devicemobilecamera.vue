<template>
    <div class="component-5578_149851">
        <div id="5578_149851" class="Pixso-symbol-5578_149851">
            <div
                id="5578_149852"
                class="Pixso-symbol-5578_149852"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149853">
                    <div
                        id="5578_149853"
                        class="Pixso-vector-5578_149853"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149858"
                class="Pixso-symbol-5578_149858"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149859">
                    <div
                        id="5578_149859"
                        class="Pixso-vector-5578_149859"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149860"
                class="Pixso-symbol-5578_149860"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149861">
                    <div
                        id="5578_149861"
                        class="Pixso-vector-5578_149861"
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
.Pixso-symbol-5578_149851 {
}
.Pixso-symbol-5578_149852 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149853 {
    width: 56.24%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector59.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 21.88%;
    right: 21.88%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-symbol-5578_149858 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149859 {
    width: 59.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector57.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 20.31%;
    right: 20.31%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-symbol-5578_149860 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149861 {
    width: 56.24%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector58.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 21.88%;
    right: 21.88%;
    top: 6.25%;
    bottom: 6.25%;
}
</style>
