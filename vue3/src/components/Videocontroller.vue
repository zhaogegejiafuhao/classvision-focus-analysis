<template>
    <div class="component-5465_53736">
        <div id="5465_53736" class="Pixso-symbol-5465_53736">
            <div
                id="5465_53735"
                class="Pixso-symbol-5465_53735 fill-gray10-83_2713 fill-transparentblack32-5571_36671"
                v-if="Type === 'Play'"
            >
                <slot name="slot_5585_1206">
                    <Play
                        id="5585_1206"
                        class="Pixso-instance-5585_1206"
                        Format="Outline"
                        Weight="Fill"
                    />
                </slot>
            </div>
            <div
                id="5465_53733"
                class="Pixso-symbol-5465_53733 fill-gray10-83_2713"
                v-if="Type === 'Pause'"
            >
                <slot name="slot_5585_1204">
                    <Pause
                        id="5585_1204"
                        class="Pixso-instance-5585_1204"
                        Format="Outline"
                        Weight="Fill"
                    />
                </slot>
            </div>
            <div
                id="5465_53732"
                class="Pixso-symbol-5465_53732 fill-gray10-83_2713"
                v-if="Type === 'Repeat'"
            >
                <slot name="slot_5585_1170">
                    <ArrowCounterClockwise
                        id="5585_1170"
                        class="Pixso-instance-5585_1170"
                        Format="Outline"
                        Weight="Fill"
                    />
                </slot>
            </div>
            <div
                id="5465_53734"
                class="Pixso-symbol-5465_53734 fill-gray10-83_2713"
                v-if="Type === 'Previous'"
            >
                <slot name="slot_5585_1200">
                    <Rewind
                        id="5585_1200"
                        class="Pixso-instance-5585_1200"
                        Format="Outline"
                        Weight="Fill"
                    />
                </slot>
            </div>
            <div
                id="5465_53731"
                class="Pixso-symbol-5465_53731 fill-gray10-83_2713"
                v-if="Type === 'Next'"
            >
                <slot name="slot_5585_1198">
                    <FastForward
                        id="5585_1198"
                        class="Pixso-instance-5585_1198"
                        Format="Outline"
                        Weight="Fill"
                    />
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Play from "@/components/Play.vue";
import Pause from "@/components/Pause.vue";
import ArrowCounterClockwise from "@/components/Arrowcounterclockwise.vue";
import Rewind from "@/components/Rewind.vue";
import FastForward from "@/components/Fastforward.vue";
const props = defineProps({
    Type: { type: String }
});
</script>
<style>
.Pixso-symbol-5465_53736 {
}
.Pixso-symbol-5465_53735 {
    width: 64px;
    height: 64px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5585_1206 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5465_53733 {
    width: 64px;
    height: 64px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5585_1204 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5465_53732 {
    width: 64px;
    height: 64px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5585_1170 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5465_53734 {
    width: 64px;
    height: 64px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5585_1200 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5465_53731 {
    width: 64px;
    height: 64px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5585_1198 {
    width: 32px;
    height: 32px;
}

.Pixso-instance-5585_1170 .Pixso-symbol-5577_144219 {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5585_1170 .Pixso-vector-5577_144220 {
    width: 81.25%;
    height: 74.99%;
    position: absolute;
    left: 6.25%;
    right: 12.5%;
    top: 12.51%;
    bottom: 12.5%;
}
.Pixso-instance-5585_1198 .Pixso-symbol-5577_147738 {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5585_1198 .Pixso-vector-5577_147739 {
    width: 87.5%;
    height: 56.26%;
    position: absolute;
    left: 12.5%;
    right: 0%;
    top: 21.87%;
    bottom: 21.87%;
}
.Pixso-instance-5585_1204 .Pixso-symbol-5577_148142 {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5585_1204 .Pixso-vector-5577_148143 {
    width: 68.74%;
    height: 75%;
    position: absolute;
    left: 15.63%;
    right: 15.63%;
    top: 12.5%;
    bottom: 12.5%;
}
.Pixso-instance-5585_1206 .Pixso-symbol-5577_148224 {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5585_1206 .Pixso-vector-5577_148225 {
    width: 68.75%;
    height: 81.26%;
    position: absolute;
    left: 25%;
    right: 6.25%;
    top: 9.37%;
    bottom: 9.37%;
}
.Pixso-instance-5585_1200 .Pixso-symbol-5577_148343 {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5585_1200 .Pixso-vector-5577_148344 {
    width: 87.5%;
    height: 56.25%;
    position: absolute;
    left: 3.12%;
    right: 9.38%;
    top: 21.87%;
    bottom: 21.88%;
}
</style>
