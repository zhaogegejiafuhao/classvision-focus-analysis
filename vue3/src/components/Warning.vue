<template>
    <div class="component-5579_153332">
        <div id="5579_153332" class="Pixso-symbol-5579_153332">
            <div
                id="5579_153333"
                class="Pixso-symbol-5579_153333"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_153334">
                    <div
                        id="5579_153334"
                        class="Pixso-vector-5579_153334"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153339"
                class="Pixso-symbol-5579_153339"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_153340">
                    <div
                        id="5579_153340"
                        class="Pixso-vector-5579_153340"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153341"
                class="Pixso-symbol-5579_153341"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_153342">
                    <div
                        id="5579_153342"
                        class="Pixso-vector-5579_153342"
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
.Pixso-symbol-5579_153332 {
}
.Pixso-symbol-5579_153333 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153334 {
    width: 87.5%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector86.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 9.37%;
    bottom: 12.5%;
}
.Pixso-symbol-5579_153339 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153340 {
    width: 90.63%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector84.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.68%;
    right: 4.69%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-symbol-5579_153341 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153342 {
    width: 87.5%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector85.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 9.37%;
    bottom: 12.5%;
}
</style>
