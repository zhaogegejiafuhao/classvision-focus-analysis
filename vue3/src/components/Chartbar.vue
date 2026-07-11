<template>
    <div class="component-5579_150825">
        <div id="5579_150825" class="Pixso-symbol-5579_150825">
            <div
                id="5579_150826"
                class="Pixso-symbol-5579_150826"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_150827">
                    <div
                        id="5579_150827"
                        class="Pixso-vector-5579_150827"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_150832"
                class="Pixso-symbol-5579_150832"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_150833">
                    <div
                        id="5579_150833"
                        class="Pixso-vector-5579_150833"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_150834"
                class="Pixso-symbol-5579_150834"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_150835">
                    <div
                        id="5579_150835"
                        class="Pixso-vector-5579_150835"
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
.Pixso-symbol-5579_150825 {
}
.Pixso-symbol-5579_150826 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_150827 {
    width: 81.24%;
    height: 71.87%;
    background-image: url(@/assets/images/Vector119.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 12.5%;
    bottom: 15.63%;
}
.Pixso-symbol-5579_150832 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_150833 {
    width: 84.38%;
    height: 75%;
    background-image: url(@/assets/images/Vector117.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 10.94%;
    bottom: 14.06%;
}
.Pixso-symbol-5579_150834 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_150835 {
    width: 81.24%;
    height: 71.87%;
    background-image: url(@/assets/images/Vector118.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 12.5%;
    bottom: 15.63%;
}
</style>
