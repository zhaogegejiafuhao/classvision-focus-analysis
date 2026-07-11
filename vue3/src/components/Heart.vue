<template>
    <div class="component-5578_148901">
        <div id="5578_148901" class="Pixso-symbol-5578_148901">
            <div
                id="5578_148902"
                class="Pixso-symbol-5578_148902"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_148903">
                    <div
                        id="5578_148903"
                        class="Pixso-vector-5578_148903"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148908"
                class="Pixso-symbol-5578_148908"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_148909">
                    <div
                        id="5578_148909"
                        class="Pixso-vector-5578_148909"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148910"
                class="Pixso-symbol-5578_148910"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_148911">
                    <div
                        id="5578_148911"
                        class="Pixso-vector-5578_148911"
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
.Pixso-symbol-5578_148901 {
}
.Pixso-symbol-5578_148902 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148903 {
    width: 87.5%;
    height: 74.98%;
    background-image: url(@/assets/images/Vector2039.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 15.63%;
    bottom: 9.39%;
}
.Pixso-symbol-5578_148908 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148909 {
    width: 90.62%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector2037.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 14.06%;
    bottom: 7.81%;
}
.Pixso-symbol-5578_148910 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148911 {
    width: 87.5%;
    height: 74.98%;
    background-image: url(@/assets/images/Vector2038.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 15.63%;
    bottom: 9.39%;
}
</style>
