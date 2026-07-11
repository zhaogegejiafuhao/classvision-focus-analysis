<template>
    <div class="component-5577_144133">
        <div id="5577_144133" class="Pixso-symbol-5577_144133">
            <div
                id="5577_144134"
                class="Pixso-symbol-5577_144134"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144135">
                    <div
                        id="5577_144135"
                        class="Pixso-vector-5577_144135"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144140"
                class="Pixso-symbol-5577_144140"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144141">
                    <div
                        id="5577_144141"
                        class="Pixso-vector-5577_144141"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144142"
                class="Pixso-symbol-5577_144142"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144143">
                    <div
                        id="5577_144143"
                        class="Pixso-vector-5577_144143"
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
.Pixso-symbol-5577_144133 {
}
.Pixso-symbol-5577_144134 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144135 {
    width: 43.76%;
    height: 81.26%;
    background-image: url(@/assets/images/Vector32.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.12%;
    right: 28.12%;
    top: 9.37%;
    bottom: 9.37%;
}
.Pixso-symbol-5577_144140 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144141 {
    width: 46.9%;
    height: 84.39%;
    background-image: url(@/assets/images/Vector30.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 26.55%;
    right: 26.55%;
    top: 7.81%;
    bottom: 7.8%;
}
.Pixso-symbol-5577_144142 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144143 {
    width: 43.76%;
    height: 81.26%;
    background-image: url(@/assets/images/Vector31.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.12%;
    right: 28.12%;
    top: 9.37%;
    bottom: 9.37%;
}
</style>
