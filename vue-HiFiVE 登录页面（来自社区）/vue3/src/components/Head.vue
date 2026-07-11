<template>
    <div class="component-2_255">
        <div
            id="2_255"
            class="Pixso-symbol-2_255 fill-material-themesyslightsurface-1_39"
        >
            <slot name="slot_1_4">
                <div id="1_4" class="Pixso-vector-1_4"></div>
            </slot>
            <div id="35_380" class="Pixso-frame-35_380">
                <slot name="slot_1_1856">
                    <Button
                        id="1_1856"
                        class="Pixso-instance-1_1856"
                        Size="36"
                        Style="ghost"
                        icon="off"
                        Status="default"
                        icononly="off"
                        @mouseover.stop="mouseover_1_1856()"
                    >
                        <template #slot_1_1462>
                            <p
                                id="6_688"
                                class="Pixso-paragraph-6_688 fill-material-themesyslighton-surface-1_40-paragraph text-cn-regular16-1_1862"
                            >
                                {{ "登录" }}
                            </p>
                        </template>
                    </Button>
                </slot>
                <slot name="slot_1_1859">
                    <Button
                        id="1_1859"
                        class="Pixso-instance-1_1859"
                        Size="36"
                        Style="filled"
                        icon="off"
                        Status="default"
                        icononly="off"
                        @mouseover.stop="mouseover_1_1859()"
                    >
                        <template #slot_1_1406>
                            <p
                                id="6_687"
                                class="Pixso-paragraph-6_687 fill-material-themesyslighton-primary-1_22-paragraph text-cn-regular16-1_1862"
                            >
                                {{ "注册" }}
                            </p>
                        </template>
                    </Button>
                </slot>
            </div>
            <div id="35_374" class="Pixso-frame-35_374">
                <slot name="slot_1_1118">
                    <p
                        id="1_1118"
                        class="Pixso-paragraph-1_1118 fill-material-themesyslighton-surface-1_40-paragraph text-cn-medium20-1_1863"
                    >
                        {{ "解决方案" }}
                    </p>
                </slot>
                <slot name="slot_1_1126">
                    <p
                        id="1_1126"
                        class="Pixso-paragraph-1_1126 fill-material-themesyslighton-surface-1_40-paragraph text-cn-medium20-1_1863"
                    >
                        {{ "音乐馆" }}
                    </p>
                </slot>
                <slot name="slot_1_1128">
                    <p
                        id="1_1128"
                        class="Pixso-paragraph-1_1128 fill-material-themesyslighton-surface-1_40-paragraph text-cn-medium20-1_1863"
                    >
                        {{ "工具" }}
                    </p>
                </slot>
                <slot name="slot_1_1130">
                    <p
                        id="1_1130"
                        class="Pixso-paragraph-1_1130 fill-material-themesyslighton-surface-1_40-paragraph text-cn-medium20-1_1863"
                    >
                        {{ "案例" }}
                    </p>
                </slot>
                <slot name="slot_1_1132">
                    <p
                        id="1_1132"
                        class="Pixso-paragraph-1_1132 fill-material-themesyslighton-surface-1_40-paragraph text-cn-medium20-1_1863"
                    >
                        {{ "文档" }}
                    </p>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Button from "@/components/Button.vue";

const mouseover_1_1859 = () => {};

const mouseover_1_1856 = () => {};
</script>
<style>
.Pixso-symbol-2_255 {
    width: calc(100% - 0px);
    height: 88px;
    overflow: hidden;
    position: relative;
    right: 0px;
    mix-blend-mode: normal;
}
.Pixso-vector-1_4 {
    width: 177px;
    height: 40px;
    background-image: url(@/assets/images/HiFivelogo.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 100px;
    top: 50%;
    transform: translateY(calc(-50% + 0px));
}
.Pixso-frame-35_380 {
    width: auto;
    height: auto;
    position: absolute;
    right: 98px;
    top: 50%;
    transform: translateY(calc(-50% + 4px));
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: flex-start;
    mix-blend-mode: normal;
}
.Pixso-instance-1_1856 {
    width: 73px;
    height: 36px;
}
.Pixso-paragraph-6_688 {
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-instance-1_1859 {
    width: 73px;
    height: 36px;
}
.Pixso-paragraph-6_687 {
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-frame-35_374 {
    width: auto;
    height: auto;
    position: absolute;
    left: 369px;
    top: 50%;
    transform: translateY(calc(-50% + 4px));
    display: flex;
    flex-direction: row;
    gap: 72px;
    align-items: flex-start;
    mix-blend-mode: normal;
}
.Pixso-paragraph-1_1118 {
    text-align: left;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-paragraph-1_1126 {
    text-align: left;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-paragraph-1_1128 {
    text-align: left;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-paragraph-1_1130 {
    text-align: left;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}
.Pixso-paragraph-1_1132 {
    text-align: left;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
    mix-blend-mode: normal;
}

.Pixso-instance-1_1859 .Pixso-symbol-1_1227 {
    width: 73px;
    height: 36px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 7px 20px 7px 20px;
    border-radius: 100px 100px 100px 100px;
}
.Pixso-instance-1_1859 .Pixso-paragraph-1_1406 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-1_1856 .Pixso-symbol-1_1263 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 8px;
    justify-content: center;
    align-items: center;
    padding: 7px 20px 7px 20px;
    border-radius: 100px 100px 100px 100px;
}
.Pixso-instance-1_1856 .stroke-wrapper-1_1263 {
    width: 73px;
    height: 36px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-1_1856 .stroke-1_1263 {
    inset: 0px;
    border-radius: 100px 100px 100px 100px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-1_1856 .Pixso-paragraph-1_1462 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
</style>
