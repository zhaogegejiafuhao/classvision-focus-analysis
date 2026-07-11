<template>
    <div class="component-5577_144532">
        <div id="5577_144532" class="Pixso-symbol-5577_144532">
            <div
                id="5577_144533"
                class="Pixso-symbol-5577_144533"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144534">
                    <div
                        id="5577_144534"
                        class="Pixso-vector-5577_144534"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144539"
                class="Pixso-symbol-5577_144539"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144540">
                    <div
                        id="5577_144540"
                        class="Pixso-vector-5577_144540"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144541"
                class="Pixso-symbol-5577_144541"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144542">
                    <div
                        id="5577_144542"
                        class="Pixso-vector-5577_144542"
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
.Pixso-symbol-5577_144532 {
}
.Pixso-symbol-5577_144533 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144534 {
    width: 75%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector44.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-symbol-5577_144539 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.65%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.92%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-symbol-5577_144541 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144542 {
    width: 75%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector43.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 18.75%;
    bottom: 18.75%;
}
</style>
