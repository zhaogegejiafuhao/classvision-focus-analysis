<template>
    <div class="component-6_392">
        <div
            id="6_392"
            class="Pixso-symbol-6_392 fill-material-themeread-onlylightsurface1-1_160"
        >
            <div id="6_391" class="Pixso-frame-6_391">
                <slot name="slot_6_384">
                    <p
                        id="6_384"
                        class="Pixso-paragraph-6_384 fill-material-themesyslightprimary-1_21-paragraph text-cn-medium20-1_1863"
                    >
                        {{ "人力成本节约" }}
                    </p>
                </slot>
                <slot name="slot_6_382">
                    <div
                        id="6_382"
                        class="Pixso-text-6_382 fill-material-themesyslighton-surface-1_40-text"
                    >
                        <p id="6_382_0" class="Pixso-paragraph-6_382_0">
                            <span id="6_382_0_1" class="Pixso-span-6_382_0_1">{{
                                "500,000 "
                            }}</span>
                            <span
                                id="6_382_0_2"
                                class="Pixso-span-6_382_0_2 text-cn-medium16-4_1302"
                                >{{ "元/年" }}</span
                            >
                        </p>
                    </div>
                </slot>
            </div>
            <slot name="slot_6_389">
                <div id="6_389" class="Pixso-vector-6_389"></div>
            </slot>
            <div id="6_390" class="Pixso-frame-6_390">
                <div class="frame-content-6_390">
                    <slot name="slot_6_386">
                        <p
                            id="6_386"
                            class="Pixso-paragraph-6_386 fill-material-themesyslighton-surface-1_40-paragraph text-cn-medium20-1_1863"
                        >
                            {{ "功能+运营服务" }}
                        </p>
                    </slot>
                    <slot name="slot_6_387">
                        <p
                            id="6_387"
                            class="Pixso-paragraph-6_387 fill-material-themesyslightsecondary-1_25-paragraph text-cn-regular14-1_1870"
                        >
                            {{
                                "自行搭建内容中台+数据中心至少需4位开发人员、自行运营需1位专业音乐内容运营人员"
                            }}
                        </p>
                    </slot>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup></script>
<style>
.Pixso-symbol-6_392 {
    width: 335px;
    height: 330px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: flex-start;
    padding: 40px 48px 40px 48px;
    border-radius: 20px 20px 20px 20px;
}
.Pixso-frame-6_391 {
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
}
.Pixso-paragraph-6_384 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-text-6_382 {
    font-size: 48px;
    font-family: "Nunito Sans-ExtraBold";
    font-weight: ExtraBold;
    display: flex;
    flex-direction: column;
    justify-content: center;
    letter-spacing: 0em;
    line-height: 56px;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: nowrap;
    flex-grow: 0;
}
.Pixso-paragraph-6_382_0 {
    line-height: 65.472px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-span-6_382_0_1 {
    font-size: 48px;
    font-family: "Nunito Sans-ExtraBold";
    font-weight: 500;
    color: rgba(0, 0, 0, 1);
    position: relative;
    flex-shrink: 0;
}
.Pixso-span-6_382_0_2 {
    text-decoration: none;
    color: rgba(92, 93, 114, 1);
    position: relative;
    flex-shrink: 0;
}
.Pixso-vector-6_389 {
    width: 100%;
    height: 1px;
    background-image: url(@/assets/images/Sep2.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-frame-6_390 {
    width: 239px;
    height: auto;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.frame-content-6_390 {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    width: 100%;
    position: relative;
}
.Pixso-paragraph-6_386 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-paragraph-6_387 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
</style>
