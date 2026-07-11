<template>
    <div class="component-6226_48938">
        <div id="6226_48938" class="Pixso-symbol-6226_48938">
            <div id="6226_48974" class="Pixso-frame-6226_48974">
                <div class="frame-content-6226_48974">
                    <div id="6226_48945" class="Pixso-frame-6226_48945">
                        <div class="frame-content-6226_48945">
                            <slot name="slot_6226_48926">
                                <p
                                    id="6226_48926"
                                    class="Pixso-paragraph-6226_48926 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                                >
                                    {{ text_6226_5 ?? "Label Title" }}
                                </p>
                            </slot>
                            <slot name="slot_6226_48942" v-if="visible_6226_6">
                                <Question
                                    id="6226_48942"
                                    class="Pixso-instance-6226_48942"
                                    Format="Outline"
                                    Weight="Bold"
                                />
                            </slot>
                        </div>
                    </div>
                    <slot name="slot_6226_48936" v-if="visible_6226_3">
                        <p
                            id="6226_48936"
                            class="Pixso-paragraph-6226_48936 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                        >
                            {{ text_6226_4 ?? "Text Description" }}
                        </p>
                    </slot>
                </div>
            </div>
            <div
                id="6226_48973"
                class="Pixso-frame-6226_48973"
                v-if="visible_6226_7"
            >
                <slot name="slot_6226_48967">
                    <Button
                        id="6226_48967"
                        class="Pixso-instance-6226_48967"
                        :visible_5588_131="false"
                        :visible_5588_152="false"
                        text_5588_173="Secondary"
                        Size="md"
                        Color="Gray"
                        Hierarchy="Link"
                        State="Default"
                    >
                        <template #slot_5603_17111>
                            <p
                                id="5603_17111"
                                class="Pixso-paragraph-5603_17111 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Secondary" }}
                            </p>
                        </template>
                    </Button>
                </slot>
                <slot name="slot_6226_48961">
                    <Button
                        id="6226_48961"
                        class="Pixso-instance-6226_48961"
                        :visible_5588_131="false"
                        :visible_5588_152="false"
                        text_5588_173="Primary"
                        Size="md"
                        Color="Brand"
                        Hierarchy="Link"
                        State="Default"
                    >
                        <template #slot_5603_17351>
                            <p
                                id="5603_17351"
                                class="Pixso-paragraph-5603_17351 fill-brand60-1257_33467-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Primary" }}
                            </p>
                        </template>
                    </Button>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Question from "@/components/Question.vue";
import Button from "@/components/Button.vue";
const props = defineProps({
    visible_6226_3: { type: Boolean, default: true },
    text_6226_4: { type: String, default: "Text Description" },
    text_6226_5: { type: String, default: "Label Title" },
    visible_6226_6: { type: Boolean, default: true },
    visible_6226_7: { type: Boolean, default: true }
});
</script>
<style>
.Pixso-symbol-6226_48938 {
    width: 260px;
    height: 78px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: flex-start;
}
.Pixso-frame-6226_48974 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-6226_48974 {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-frame-6226_48945 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.frame-content-6226_48945 {
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6226_48926 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6226_48942 {
    width: 20px;
    height: 20px;
}
.Pixso-paragraph-6226_48936 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-frame-6226_48973 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: flex-start;
}
.Pixso-instance-6226_48967 {
    width: 74px;
    height: 20px;
}
.Pixso-paragraph-5603_17111 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-6226_48961 {
    width: 52px;
    height: 20px;
}
.Pixso-paragraph-5603_17351 {
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}

.Pixso-instance-6226_48942 .Pixso-symbol-5579_153182 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-6226_48942 .Pixso-vector-5579_153183 {
    width: 84.38%;
    height: 84.38%;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-instance-6226_48967 .Pixso-symbol-5603_17109 {
    width: 74px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6226_48967 .Pixso-instance-5603_17110 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6226_48967 .Pixso-paragraph-5603_17111 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6226_48967 .Pixso-instance-5603_17112 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6226_48961 .Pixso-symbol-5603_17349 {
    width: 52px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
}
.Pixso-instance-6226_48961 .Pixso-instance-5603_17350 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6226_48961 .Pixso-paragraph-5603_17351 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-6226_48961 .Pixso-instance-5603_17352 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-6226_48961
    .Pixso-instance-5603_17352
    .Pixso-vector-5577_144540 {
    width: 78.14%;
    height: 65.64%;
    background-image: url(@/assets/images/Vector42.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 12.75%;
    top: 14.31%;
    bottom: 20.05%;
}
</style>
