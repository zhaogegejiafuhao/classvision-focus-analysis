<template>
    <div class="component-6169_18240">
        <div id="6169_18240" class="Pixso-symbol-6169_18240">
            <div
                id="6169_18239"
                class="Pixso-symbol-6169_18239"
                v-if="Size === 'sm'"
            >
                <slot name="slot_6169_18231">
                    <Avatar
                        id="6169_18231"
                        class="Pixso-instance-6169_18231"
                        Size="sm"
                        Type="Image"
                        Indicator="None"
                    />
                </slot>
                <div id="6169_18232" class="Pixso-frame-6169_18232">
                    <slot name="slot_6169_18233">
                        <p
                            id="6169_18233"
                            class="Pixso-paragraph-6169_18233 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_6169_22 ?? "X_AE_A-13" }}
                        </p>
                    </slot>
                    <slot name="slot_6169_18234" v-if="visible_6169_7">
                        <p
                            id="6169_18234"
                            class="Pixso-paragraph-6169_18234 fill-gray60-83_2722-paragraph text-paragraphxs-20_2108"
                        >
                            {{ text_6169_12 ?? "Product Designer, slothUI" }}
                        </p>
                    </slot>
                </div>
            </div>
            <div
                id="6169_18238"
                class="Pixso-symbol-6169_18238"
                v-if="Size === 'md'"
            >
                <slot name="slot_6169_18226">
                    <Avatar
                        id="6169_18226"
                        class="Pixso-instance-6169_18226"
                        Size="md"
                        Type="Image"
                        Indicator="None"
                    />
                </slot>
                <div id="6169_18227" class="Pixso-frame-6169_18227">
                    <slot name="slot_6169_18228">
                        <p
                            id="6169_18228"
                            class="Pixso-paragraph-6169_18228 fill-gray80-32_4123-paragraph text-text-smbold-423_3208"
                        >
                            {{ text_6169_22 ?? "X_AE_A-13" }}
                        </p>
                    </slot>
                    <slot name="slot_6169_18229" v-if="visible_6169_7">
                        <p
                            id="6169_18229"
                            class="Pixso-paragraph-6169_18229 fill-gray60-83_2722-paragraph text-paragraphsm-20_2107"
                        >
                            {{ text_6169_12 ?? "Product Designer, slothUI" }}
                        </p>
                    </slot>
                </div>
            </div>
            <div
                id="6169_18236"
                class="Pixso-symbol-6169_18236"
                v-if="Size === 'lg'"
            >
                <slot name="slot_6169_18221">
                    <Avatar
                        id="6169_18221"
                        class="Pixso-instance-6169_18221"
                        Size="lg"
                        Type="Image"
                        Indicator="None"
                    />
                </slot>
                <div id="6169_18222" class="Pixso-frame-6169_18222">
                    <slot name="slot_6169_18223">
                        <p
                            id="6169_18223"
                            class="Pixso-paragraph-6169_18223 fill-gray80-32_4123-paragraph text-text-mdbold-423_3205"
                        >
                            {{ text_6169_22 ?? "X_AE_A-13" }}
                        </p>
                    </slot>
                    <slot name="slot_6169_18224" v-if="visible_6169_7">
                        <p
                            id="6169_18224"
                            class="Pixso-paragraph-6169_18224 fill-gray60-83_2722-paragraph text-paragraphmd-20_2106"
                        >
                            {{ text_6169_12 ?? "Product Designer, slothUI" }}
                        </p>
                    </slot>
                </div>
            </div>
            <div
                id="6169_18237"
                class="Pixso-symbol-6169_18237"
                v-if="Size === 'xl'"
            >
                <slot name="slot_6168_7889">
                    <Avatar
                        id="6168_7889"
                        class="Pixso-instance-6168_7889"
                        Size="xl"
                        Type="Image"
                        Indicator="None"
                    />
                </slot>
                <div id="6168_7890" class="Pixso-frame-6168_7890">
                    <slot name="slot_6168_7891">
                        <p
                            id="6168_7891"
                            class="Pixso-paragraph-6168_7891 fill-gray80-32_4123-paragraph text-text-lgbold-423_3202"
                        >
                            {{ text_6169_22 ?? "X_AE_A-13" }}
                        </p>
                    </slot>
                    <slot name="slot_6168_7892" v-if="visible_6169_7">
                        <p
                            id="6168_7892"
                            class="Pixso-paragraph-6168_7892 fill-gray60-83_2722-paragraph text-paragraphmd-20_2106"
                        >
                            {{ text_6169_12 ?? "Product Designer, slothUI" }}
                        </p>
                    </slot>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Avatar from "@/components/Avatar.vue";
const props = defineProps({
    visible_6169_7: { type: Boolean, default: true },
    text_6169_12: { type: String, default: "Product Designer, slothUI" },
    text_6169_22: { type: String, default: "X_AE_A-13" },
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-6169_18240 {
}
.Pixso-symbol-6169_18239 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-6169_18231 {
    width: 32px;
    height: 32px;
}
.Pixso-frame-6169_18232 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-paragraph-6169_18233 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-6169_18234 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-6169_18238 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-6169_18226 {
    width: 40px;
    height: 40px;
}
.Pixso-frame-6169_18227 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-paragraph-6169_18228 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-6169_18229 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-6169_18236 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-6169_18221 {
    width: 48px;
    height: 48px;
}
.Pixso-frame-6169_18222 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-paragraph-6169_18223 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-6169_18224 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-6169_18237 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-6168_7889 {
    width: 56px;
    height: 56px;
}
.Pixso-frame-6168_7890 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.Pixso-paragraph-6168_7891 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-6168_7892 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}

.Pixso-instance-6169_18231 .Pixso-symbol-5468_1032 {
    width: 32px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    border-radius: 61.5px 61.5px 61.5px 61.5px;
}
.Pixso-instance-6169_18226 .Pixso-symbol-5468_1033 {
    width: 40px;
    height: 40px;
    position: relative;
    flex-shrink: 0;
    border-radius: 76.875px 76.875px 76.875px 76.875px;
}
.Pixso-instance-6169_18221 .Pixso-symbol-5468_1029 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
    border-radius: 92.25px 92.25px 92.25px 92.25px;
}
.Pixso-instance-6168_7889 .Pixso-symbol-5468_1030 {
    width: 56px;
    height: 56px;
    position: relative;
    flex-shrink: 0;
    border-radius: 107.625px 107.625px 107.625px 107.625px;
}
</style>
