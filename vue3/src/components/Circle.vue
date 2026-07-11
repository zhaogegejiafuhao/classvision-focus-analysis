<template>
    <div class="component-5578_148934">
        <div id="5578_148934" class="Pixso-symbol-5578_148934">
            <div
                id="5578_148935"
                class="Pixso-symbol-5578_148935"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_148936">
                    <div
                        id="5578_148936"
                        class="Pixso-vector-5578_148936"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148941"
                class="Pixso-symbol-5578_148941"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_148942">
                    <div
                        id="5578_148942"
                        class="Pixso-vector-5578_148942"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148943"
                class="Pixso-symbol-5578_148943"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_148944">
                    <div
                        id="5578_148944"
                        class="Pixso-vector-5578_148944"
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
.Pixso-symbol-5578_148934 {
}
.Pixso-symbol-5578_148935 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148936 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector11.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5578_148941 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148942 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector9.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5578_148943 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148944 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector10.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
