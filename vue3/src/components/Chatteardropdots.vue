<template>
    <div class="component-5577_146636">
        <div id="5577_146636" class="Pixso-symbol-5577_146636">
            <div
                id="5577_146637"
                class="Pixso-symbol-5577_146637"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_146638">
                    <div
                        id="5577_146638"
                        class="Pixso-vector-5577_146638"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_146643"
                class="Pixso-symbol-5577_146643"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_146644">
                    <div
                        id="5577_146644"
                        class="Pixso-vector-5577_146644"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_146645"
                class="Pixso-symbol-5577_146645"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_146646">
                    <div
                        id="5577_146646"
                        class="Pixso-vector-5577_146646"
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
.Pixso-symbol-5577_146636 {
}
.Pixso-symbol-5577_146637 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_146638 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector329.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 9.38%;
    top: 9.38%;
    bottom: 12.5%;
}
.Pixso-symbol-5577_146643 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_146644 {
    width: 81.25%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector327.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 7.81%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-symbol-5577_146645 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_146646 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector328.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 9.38%;
    top: 9.38%;
    bottom: 12.5%;
}
</style>
