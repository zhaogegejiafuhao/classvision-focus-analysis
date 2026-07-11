<template>
    <div class="component-5577_147729">
        <div id="5577_147729" class="Pixso-symbol-5577_147729">
            <div
                id="5577_147730"
                class="Pixso-symbol-5577_147730"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_147731">
                    <div
                        id="5577_147731"
                        class="Pixso-vector-5577_147731"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_147736"
                class="Pixso-symbol-5577_147736"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_147737">
                    <div
                        id="5577_147737"
                        class="Pixso-vector-5577_147737"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_147738"
                class="Pixso-symbol-5577_147738"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_147739">
                    <div
                        id="5577_147739"
                        class="Pixso-vector-5577_147739"
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
.Pixso-symbol-5577_147729 {
}
.Pixso-symbol-5577_147730 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_147731 {
    width: 87.5%;
    height: 56.25%;
    background-image: url(@/assets/images/Vector332.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 0%;
    top: 21.87%;
    bottom: 21.88%;
}
.Pixso-symbol-5577_147736 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_147737 {
    width: 90.62%;
    height: 59.38%;
    background-image: url(@/assets/images/Vector330.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 0%;
    top: 20.31%;
    bottom: 20.31%;
}
.Pixso-symbol-5577_147738 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_147739 {
    width: 87.5%;
    height: 56.26%;
    background-image: url(@/assets/images/Vector331.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 0%;
    top: 21.87%;
    bottom: 21.87%;
}
</style>
