<template>
    <div class="component-5577_148133">
        <div id="5577_148133" class="Pixso-symbol-5577_148133">
            <div
                id="5577_148134"
                class="Pixso-symbol-5577_148134"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_148135">
                    <div
                        id="5577_148135"
                        class="Pixso-vector-5577_148135"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_148140"
                class="Pixso-symbol-5577_148140"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_148141">
                    <div
                        id="5577_148141"
                        class="Pixso-vector-5577_148141"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_148142"
                class="Pixso-symbol-5577_148142"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_148143">
                    <div
                        id="5577_148143"
                        class="Pixso-vector-5577_148143"
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
.Pixso-symbol-5577_148133 {
}
.Pixso-symbol-5577_148134 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148135 {
    width: 68.74%;
    height: 75%;
    background-image: url(@/assets/images/Vector350.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 12.5%;
    bottom: 12.5%;
}
.Pixso-symbol-5577_148140 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148141 {
    width: 71.88%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector348.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-symbol-5577_148142 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148143 {
    width: 68.74%;
    height: 75%;
    background-image: url(@/assets/images/Vector349.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
