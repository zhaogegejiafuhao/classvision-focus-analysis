<template>
    <div class="component-5606_17912">
        <div id="5606_17912" class="Pixso-symbol-5606_17912">
            <div
                id="5606_17910"
                class="Pixso-symbol-5606_17910"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5606_17906">
                    <div id="5606_17906" class="Pixso-vector-5606_17906"></div>
                </slot>
            </div>
            <div
                id="5606_17909"
                class="Pixso-symbol-5606_17909"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5606_17908">
                    <div id="5606_17908" class="Pixso-vector-5606_17908"></div>
                </slot>
            </div>
            <div
                id="5606_17911"
                class="Pixso-symbol-5606_17911"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5606_17904">
                    <div id="5606_17904" class="Pixso-vector-5606_17904"></div>
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
.Pixso-symbol-5606_17912 {
}
.Pixso-symbol-5606_17910 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5606_17906 {
    width: 73.44%;
    height: 79.69%;
    background-image: url(@/assets/images/Vector2042.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 13.28%;
    right: 13.28%;
    top: 7.03%;
    bottom: 13.28%;
}
.Pixso-symbol-5606_17909 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5606_17908 {
    width: 78.12%;
    height: 85.93%;
    background-image: url(@/assets/images/Vector2041.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 3.13%;
    bottom: 10.94%;
}
.Pixso-symbol-5606_17911 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5606_17904 {
    width: 75%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector2040.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 6.25%;
    bottom: 12.5%;
}
</style>
