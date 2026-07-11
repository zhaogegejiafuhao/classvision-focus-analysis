<template>
    <div class="component-5489_8980">
        <div id="5489_8980" class="Pixso-symbol-5489_8980">
            <div
                id="6456_109607"
                class="Pixso-symbol-6456_109607"
                v-if="Size === 'xs'"
            >
                <div
                    id="6456_109608"
                    class="Pixso-frame-6456_109608 fill-success50-1636_81205 fill-gray30-35_1481"
                ></div>
            </div>
            <div
                id="5489_8978"
                class="Pixso-symbol-5489_8978"
                v-if="Size === 'sm'"
            >
                <div
                    id="5490_8987"
                    class="Pixso-frame-5490_8987 fill-success50-1636_81205 fill-brand40-1257_33464 fill-gray0-white-67_3285 fill-brand60-1257_33467 fill-brand30-1257_33463 fill-destructive50-423_3219 fill-destructive40-32_4110 fill-warning50-423_3213 fill-warning40-428_4549 fill-success40-1636_81204 fill-destructive30-423_3220 fill-warning30-32_4109 fill-gray60-83_2722 fill-success30-1636_81203 fill-gray40-83_2714 fill-gray30-35_1481"
                ></div>
            </div>
            <div
                id="5489_8979"
                class="Pixso-symbol-5489_8979"
                v-if="Size === 'md'"
            >
                <div
                    id="5490_8989"
                    class="Pixso-frame-5490_8989 fill-success50-1636_81205"
                ></div>
            </div>
            <div
                id="5489_8977"
                class="Pixso-symbol-5489_8977"
                v-if="Size === 'lg'"
            >
                <div
                    id="5490_8990"
                    class="Pixso-frame-5490_8990 fill-success50-1636_81205"
                ></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-5489_8980 {
}
.Pixso-symbol-6456_109607 {
    width: 6px;
    height: 6px;
    position: relative;
}
.Pixso-frame-6456_109608 {
    width: 66.66%;
    height: 66.66%;
    overflow: hidden;
    position: absolute;
    left: 16.67%;
    right: 16.67%;
    top: 16.67%;
    bottom: 16.67%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-symbol-5489_8978 {
    width: 8px;
    height: 8px;
    position: relative;
}
.Pixso-frame-5490_8987 {
    width: 75%;
    height: 75%;
    overflow: hidden;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-symbol-5489_8979 {
    width: 10px;
    height: 10px;
    position: relative;
}
.Pixso-frame-5490_8989 {
    width: 80%;
    height: 80%;
    overflow: hidden;
    position: absolute;
    left: 10%;
    right: 10%;
    top: 10%;
    bottom: 10%;
    border-radius: 9999px 9999px 9999px 9999px;
}
.Pixso-symbol-5489_8977 {
    width: 12px;
    height: 12px;
    position: relative;
    background-color: transparent;
}
.Pixso-frame-5490_8990 {
    width: 83.34%;
    height: 83.34%;
    overflow: hidden;
    position: absolute;
    left: 8.33%;
    right: 8.33%;
    top: 8.33%;
    bottom: 8.33%;
    border-radius: 9999px 9999px 9999px 9999px;
}
</style>
