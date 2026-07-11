<template>
    <div class="component-5579_153218">
        <div id="5579_153218" class="Pixso-symbol-5579_153218">
            <div
                id="5579_153219"
                class="Pixso-symbol-5579_153219"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_153220">
                    <div
                        id="5579_153220"
                        class="Pixso-vector-5579_153220"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153225"
                class="Pixso-symbol-5579_153225"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_153226">
                    <div
                        id="5579_153226"
                        class="Pixso-vector-5579_153226"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153227"
                class="Pixso-symbol-5579_153227"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_153228">
                    <div
                        id="5579_153228"
                        class="Pixso-vector-5579_153228"
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
.Pixso-symbol-5579_153218 {
}
.Pixso-symbol-5579_153219 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153220 {
    width: 50%;
    height: 71.87%;
    background-image: url(@/assets/images/Vector80.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 25%;
    right: 25%;
    top: 15.63%;
    bottom: 12.5%;
}
.Pixso-symbol-5579_153225 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153226 {
    width: 53.12%;
    height: 75%;
    background-image: url(@/assets/images/Vector78.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 23.44%;
    right: 23.44%;
    top: 14.06%;
    bottom: 10.94%;
}
.Pixso-symbol-5579_153227 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153228 {
    width: 68.74%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector79.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
