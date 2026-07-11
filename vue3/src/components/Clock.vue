<template>
    <div class="component-5578_148863">
        <div id="5578_148863" class="Pixso-symbol-5578_148863">
            <div
                id="5578_148864"
                class="Pixso-symbol-5578_148864"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_148865">
                    <div
                        id="5578_148865"
                        class="Pixso-vector-5578_148865"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148870"
                class="Pixso-symbol-5578_148870"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_148871">
                    <div
                        id="5578_148871"
                        class="Pixso-vector-5578_148871"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148872"
                class="Pixso-symbol-5578_148872"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_148873">
                    <div
                        id="5578_148873"
                        class="Pixso-vector-5578_148873"
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
.Pixso-symbol-5578_148863 {
}
.Pixso-symbol-5578_148864 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148865 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector2036.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5578_148870 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148871 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector2034.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5578_148872 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148873 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector2035.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
