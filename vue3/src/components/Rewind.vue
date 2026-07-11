<template>
    <div class="component-5577_148334">
        <div id="5577_148334" class="Pixso-symbol-5577_148334">
            <div
                id="5577_148335"
                class="Pixso-symbol-5577_148335"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_148336">
                    <div
                        id="5577_148336"
                        class="Pixso-vector-5577_148336"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_148341"
                class="Pixso-symbol-5577_148341"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_148342">
                    <div
                        id="5577_148342"
                        class="Pixso-vector-5577_148342"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_148343"
                class="Pixso-symbol-5577_148343"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_148344">
                    <div
                        id="5577_148344"
                        class="Pixso-vector-5577_148344"
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
.Pixso-symbol-5577_148334 {
}
.Pixso-symbol-5577_148335 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148336 {
    width: 87.5%;
    height: 56.26%;
    background-image: url(@/assets/images/Vector374.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.12%;
    right: 9.38%;
    top: 21.87%;
    bottom: 21.87%;
}
.Pixso-symbol-5577_148341 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148342 {
    width: 90.63%;
    height: 59.39%;
    background-image: url(@/assets/images/Vector372.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 1.56%;
    right: 7.81%;
    top: 20.31%;
    bottom: 20.3%;
}
.Pixso-symbol-5577_148343 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148344 {
    width: 87.5%;
    height: 56.25%;
    background-image: url(@/assets/images/Vector373.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.12%;
    right: 9.38%;
    top: 21.87%;
    bottom: 21.88%;
}
</style>
