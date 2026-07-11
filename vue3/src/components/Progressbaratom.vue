<template>
    <div class="component-1264_9818">
        <div id="1264_9818" class="Pixso-symbol-1264_9818">
            <div
                id="1264_9819"
                class="Pixso-symbol-1264_9819 fill-gray60-83_2722 fill-gray20-36_1844 fill-brand60-1257_33467"
                v-if="Size === 'lg' && Style === 'Fill'"
            ></div>
            <div
                id="1264_9820"
                class="stroke-wrapper-1264_9820"
                v-if="Size === 'lg' && Style === 'Outlined'"
            >
                <div class="Pixso-symbol-1264_9820"></div>
                <div class="stroke-1264_9820 stroke-gray60-83_2722"></div>
            </div>
            <div
                id="5555_43901"
                class="Pixso-symbol-5555_43901 fill-gray20-36_1844"
                v-if="Size === 'lg' && Style === 'Subtle'"
            ></div>
            <div
                id="1264_9823"
                class="Pixso-symbol-1264_9823 fill-gray60-83_2722 fill-gray20-36_1844 fill-brand60-1257_33467"
                v-if="Size === 'md' && Style === 'Fill'"
            ></div>
            <div
                id="1264_9824"
                class="stroke-wrapper-1264_9824"
                v-if="Size === 'md' && Style === 'Outlined'"
            >
                <div class="Pixso-symbol-1264_9824"></div>
                <div class="stroke-1264_9824 stroke-gray60-83_2722"></div>
            </div>
            <div
                id="5555_43903"
                class="Pixso-symbol-5555_43903 fill-gray20-36_1844"
                v-if="Size === 'md' && Style === 'Subtle'"
            ></div>
            <div
                id="1264_9827"
                class="Pixso-symbol-1264_9827 fill-gray60-83_2722 fill-gray20-36_1844 fill-brand60-1257_33467 fill-success50-1636_81205 fill-gray30-35_1481"
                v-if="Size === 'sm' && Style === 'Fill'"
            ></div>
            <div
                id="1264_9828"
                class="stroke-wrapper-1264_9828"
                v-if="Size === 'sm' && Style === 'Outlined'"
            >
                <div class="Pixso-symbol-1264_9828"></div>
                <div class="stroke-1264_9828 stroke-gray60-83_2722"></div>
            </div>
            <div
                id="5555_43905"
                class="Pixso-symbol-5555_43905 fill-gray20-36_1844"
                v-if="Size === 'sm' && Style === 'Subtle'"
            ></div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Size: { type: String },
    Style: { type: String }
});
</script>
<style>
.Pixso-symbol-1264_9818 {
}
.Pixso-symbol-1264_9819 {
    width: 36px;
    height: 12px;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-symbol-1264_9820 {
    width: 100%;
    height: 100%;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-1264_9820 {
    position: relative;
    width: 36px;
    height: 12px;
}
.stroke-1264_9820 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5555_43901 {
    width: 36px;
    height: 12px;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-symbol-1264_9823 {
    width: 36px;
    height: 8px;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-symbol-1264_9824 {
    width: 100%;
    height: 100%;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-1264_9824 {
    position: relative;
    width: 36px;
    height: 8px;
}
.stroke-1264_9824 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5555_43903 {
    width: 36px;
    height: 8px;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-symbol-1264_9827 {
    width: 36px;
    height: 4px;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-symbol-1264_9828 {
    width: 100%;
    height: 100%;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-1264_9828 {
    position: relative;
    width: 36px;
    height: 4px;
}
.stroke-1264_9828 {
    position: absolute;
    inset: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-symbol-5555_43905 {
    width: 36px;
    height: 4px;
    position: relative;
    border-radius: 1234px 1234px 1234px 1234px;
}
</style>
