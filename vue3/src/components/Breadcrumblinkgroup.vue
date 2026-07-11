<template>
    <div class="component-5594_10959">
        <div id="5594_10959" class="Pixso-symbol-5594_10959">
            <div
                id="5594_10952"
                class="Pixso-symbol-5594_10952"
                v-if="
                    Style === 'Default' &&
                    IsBoxed === 'False' &&
                    Divider === 'Icon'
                "
            >
                <slot name="slot_5594_10902">
                    <ButtonIcon
                        id="5594_10902"
                        class="Pixso-instance-5594_10902"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_10926">
                    <BreadcrumbIndicator
                        id="5594_10926"
                        class="Pixso-instance-5594_10926"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_10874">
                    <BreadcrumbLinkItem
                        id="5594_10874"
                        class="Pixso-instance-5594_10874"
                        :visible_5594_0="false"
                        text_5594_7="Link Item"
                        State="Default"
                        Fill="None"
                    >
                        <template #slot_5522_33761>
                            <p
                                id="5522_33761"
                                class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Link Item" }}
                            </p>
                        </template>
                    </BreadcrumbLinkItem>
                </slot>
                <slot name="slot_5594_10912">
                    <BreadcrumbIndicator
                        id="5594_10912"
                        class="Pixso-instance-5594_10912"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_10915">
                    <BreadcrumbLinkItem
                        id="5594_10915"
                        class="Pixso-instance-5594_10915"
                        :visible_5594_0="false"
                        text_5594_7="Link Item"
                        State="Default"
                        Fill="None"
                    >
                        <template #slot_5522_33761>
                            <p
                                id="5522_33761"
                                class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Link Item" }}
                            </p>
                        </template>
                    </BreadcrumbLinkItem>
                </slot>
                <slot name="slot_5594_10921">
                    <BreadcrumbIndicator
                        id="5594_10921"
                        class="Pixso-instance-5594_10921"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_10918">
                    <BreadcrumbLinkItem
                        id="5594_10918"
                        class="Pixso-instance-5594_10918"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="None"
                    />
                </slot>
            </div>
            <div
                id="5594_11351"
                class="Pixso-symbol-5594_11351"
                v-if="
                    Style === 'Default' &&
                    IsBoxed === 'False' &&
                    Divider === 'Slash'
                "
            >
                <slot name="slot_5594_11352">
                    <ButtonIcon
                        id="5594_11352"
                        class="Pixso-instance-5594_11352"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11353">
                    <BreadcrumbIndicator
                        id="5594_11353"
                        class="Pixso-instance-5594_11353"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11354">
                    <BreadcrumbLinkItem
                        id="5594_11354"
                        class="Pixso-instance-5594_11354"
                        :visible_5594_0="false"
                        text_5594_7="Link Item"
                        State="Default"
                        Fill="None"
                    >
                        <template #slot_5522_33761>
                            <p
                                id="5522_33761"
                                class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Link Item" }}
                            </p>
                        </template>
                    </BreadcrumbLinkItem>
                </slot>
                <slot name="slot_5594_11355">
                    <BreadcrumbIndicator
                        id="5594_11355"
                        class="Pixso-instance-5594_11355"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11356">
                    <BreadcrumbLinkItem
                        id="5594_11356"
                        class="Pixso-instance-5594_11356"
                        :visible_5594_0="false"
                        text_5594_7="Link Item"
                        State="Default"
                        Fill="None"
                    >
                        <template #slot_5522_33761>
                            <p
                                id="5522_33761"
                                class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Link Item" }}
                            </p>
                        </template>
                    </BreadcrumbLinkItem>
                </slot>
                <slot name="slot_5594_11357">
                    <BreadcrumbIndicator
                        id="5594_11357"
                        class="Pixso-instance-5594_11357"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11358">
                    <BreadcrumbLinkItem
                        id="5594_11358"
                        class="Pixso-instance-5594_11358"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="None"
                    />
                </slot>
            </div>
            <div
                id="5594_11633"
                class="Pixso-symbol-5594_11633"
                v-if="
                    Style === 'Default' &&
                    IsBoxed === 'False' &&
                    Divider === 'Colon'
                "
            >
                <slot name="slot_5594_11634">
                    <ButtonIcon
                        id="5594_11634"
                        class="Pixso-instance-5594_11634"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11635">
                    <BreadcrumbIndicator
                        id="5594_11635"
                        class="Pixso-instance-5594_11635"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11636">
                    <BreadcrumbLinkItem
                        id="5594_11636"
                        class="Pixso-instance-5594_11636"
                        :visible_5594_0="false"
                        text_5594_7="Link Item"
                        State="Default"
                        Fill="None"
                    >
                        <template #slot_5522_33761>
                            <p
                                id="5522_33761"
                                class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Link Item" }}
                            </p>
                        </template>
                    </BreadcrumbLinkItem>
                </slot>
                <slot name="slot_5594_11637">
                    <BreadcrumbIndicator
                        id="5594_11637"
                        class="Pixso-instance-5594_11637"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11638">
                    <BreadcrumbLinkItem
                        id="5594_11638"
                        class="Pixso-instance-5594_11638"
                        :visible_5594_0="false"
                        text_5594_7="Link Item"
                        State="Default"
                        Fill="None"
                    >
                        <template #slot_5522_33761>
                            <p
                                id="5522_33761"
                                class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                            >
                                {{ "Link Item" }}
                            </p>
                        </template>
                    </BreadcrumbLinkItem>
                </slot>
                <slot name="slot_5594_11639">
                    <BreadcrumbIndicator
                        id="5594_11639"
                        class="Pixso-instance-5594_11639"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11640">
                    <BreadcrumbLinkItem
                        id="5594_11640"
                        class="Pixso-instance-5594_11640"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="None"
                    />
                </slot>
            </div>
            <div
                id="5594_11144"
                class="stroke-wrapper-5594_11144"
                v-if="
                    Style === 'Default' &&
                    IsBoxed === 'True' &&
                    Divider === 'Icon'
                "
            >
                <div class="Pixso-symbol-5594_11144">
                    <slot name="slot_5594_11145">
                        <ButtonIcon
                            id="5594_11145"
                            class="Pixso-instance-5594_11145"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11146">
                        <BreadcrumbIndicator
                            id="5594_11146"
                            class="Pixso-instance-5594_11146"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11147">
                        <BreadcrumbLinkItem
                            id="5594_11147"
                            class="Pixso-instance-5594_11147"
                            :visible_5594_0="false"
                            text_5594_7="Link Item"
                            State="Default"
                            Fill="None"
                        >
                            <template #slot_5522_33761>
                                <p
                                    id="5522_33761"
                                    class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Link Item" }}
                                </p>
                            </template>
                        </BreadcrumbLinkItem>
                    </slot>
                    <slot name="slot_5594_11148">
                        <BreadcrumbIndicator
                            id="5594_11148"
                            class="Pixso-instance-5594_11148"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11149">
                        <BreadcrumbLinkItem
                            id="5594_11149"
                            class="Pixso-instance-5594_11149"
                            :visible_5594_0="false"
                            text_5594_7="Link Item"
                            State="Default"
                            Fill="None"
                        >
                            <template #slot_5522_33761>
                                <p
                                    id="5522_33761"
                                    class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Link Item" }}
                                </p>
                            </template>
                        </BreadcrumbLinkItem>
                    </slot>
                    <slot name="slot_5594_11150">
                        <BreadcrumbIndicator
                            id="5594_11150"
                            class="Pixso-instance-5594_11150"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11151">
                        <BreadcrumbLinkItem
                            id="5594_11151"
                            class="Pixso-instance-5594_11151"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="None"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11144 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11359"
                class="stroke-wrapper-5594_11359"
                v-if="
                    Style === 'Default' &&
                    IsBoxed === 'True' &&
                    Divider === 'Slash'
                "
            >
                <div class="Pixso-symbol-5594_11359">
                    <slot name="slot_5594_11360">
                        <ButtonIcon
                            id="5594_11360"
                            class="Pixso-instance-5594_11360"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11361">
                        <BreadcrumbIndicator
                            id="5594_11361"
                            class="Pixso-instance-5594_11361"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11362">
                        <BreadcrumbLinkItem
                            id="5594_11362"
                            class="Pixso-instance-5594_11362"
                            :visible_5594_0="false"
                            text_5594_7="Link Item"
                            State="Default"
                            Fill="None"
                        >
                            <template #slot_5522_33761>
                                <p
                                    id="5522_33761"
                                    class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Link Item" }}
                                </p>
                            </template>
                        </BreadcrumbLinkItem>
                    </slot>
                    <slot name="slot_5594_11363">
                        <BreadcrumbIndicator
                            id="5594_11363"
                            class="Pixso-instance-5594_11363"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11364">
                        <BreadcrumbLinkItem
                            id="5594_11364"
                            class="Pixso-instance-5594_11364"
                            :visible_5594_0="false"
                            text_5594_7="Link Item"
                            State="Default"
                            Fill="None"
                        >
                            <template #slot_5522_33761>
                                <p
                                    id="5522_33761"
                                    class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Link Item" }}
                                </p>
                            </template>
                        </BreadcrumbLinkItem>
                    </slot>
                    <slot name="slot_5594_11365">
                        <BreadcrumbIndicator
                            id="5594_11365"
                            class="Pixso-instance-5594_11365"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11366">
                        <BreadcrumbLinkItem
                            id="5594_11366"
                            class="Pixso-instance-5594_11366"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="None"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11359 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11641"
                class="stroke-wrapper-5594_11641"
                v-if="
                    Style === 'Default' &&
                    IsBoxed === 'True' &&
                    Divider === 'Colon'
                "
            >
                <div class="Pixso-symbol-5594_11641">
                    <slot name="slot_5594_11642">
                        <ButtonIcon
                            id="5594_11642"
                            class="Pixso-instance-5594_11642"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11643">
                        <BreadcrumbIndicator
                            id="5594_11643"
                            class="Pixso-instance-5594_11643"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11644">
                        <BreadcrumbLinkItem
                            id="5594_11644"
                            class="Pixso-instance-5594_11644"
                            :visible_5594_0="false"
                            text_5594_7="Link Item"
                            State="Default"
                            Fill="None"
                        >
                            <template #slot_5522_33761>
                                <p
                                    id="5522_33761"
                                    class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Link Item" }}
                                </p>
                            </template>
                        </BreadcrumbLinkItem>
                    </slot>
                    <slot name="slot_5594_11645">
                        <BreadcrumbIndicator
                            id="5594_11645"
                            class="Pixso-instance-5594_11645"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11646">
                        <BreadcrumbLinkItem
                            id="5594_11646"
                            class="Pixso-instance-5594_11646"
                            :visible_5594_0="false"
                            text_5594_7="Link Item"
                            State="Default"
                            Fill="None"
                        >
                            <template #slot_5522_33761>
                                <p
                                    id="5522_33761"
                                    class="Pixso-paragraph-5522_33761 fill-gray60-83_2722-paragraph text-text-smbold-423_3208"
                                >
                                    {{ "Link Item" }}
                                </p>
                            </template>
                        </BreadcrumbLinkItem>
                    </slot>
                    <slot name="slot_5594_11647">
                        <BreadcrumbIndicator
                            id="5594_11647"
                            class="Pixso-instance-5594_11647"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11648">
                        <BreadcrumbLinkItem
                            id="5594_11648"
                            class="Pixso-instance-5594_11648"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="None"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11641 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_10988"
                class="Pixso-symbol-5594_10988"
                v-if="
                    Style === 'Fill' &&
                    IsBoxed === 'False' &&
                    Divider === 'Icon'
                "
            >
                <slot name="slot_5594_10989">
                    <ButtonIcon
                        id="5594_10989"
                        class="Pixso-instance-5594_10989"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_10990">
                    <BreadcrumbIndicator
                        id="5594_10990"
                        class="Pixso-instance-5594_10990"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_10991">
                    <BreadcrumbLinkItem
                        id="5594_10991"
                        class="Pixso-instance-5594_10991"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Subtle"
                    />
                </slot>
                <slot name="slot_5594_10992">
                    <BreadcrumbIndicator
                        id="5594_10992"
                        class="Pixso-instance-5594_10992"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_10993">
                    <BreadcrumbLinkItem
                        id="5594_10993"
                        class="Pixso-instance-5594_10993"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Subtle"
                    />
                </slot>
                <slot name="slot_5594_10994">
                    <BreadcrumbIndicator
                        id="5594_10994"
                        class="Pixso-instance-5594_10994"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_10995">
                    <BreadcrumbLinkItem
                        id="5594_10995"
                        class="Pixso-instance-5594_10995"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="Subtle"
                    />
                </slot>
            </div>
            <div
                id="5594_11367"
                class="Pixso-symbol-5594_11367"
                v-if="
                    Style === 'Fill' &&
                    IsBoxed === 'False' &&
                    Divider === 'Slash'
                "
            >
                <slot name="slot_5594_11368">
                    <ButtonIcon
                        id="5594_11368"
                        class="Pixso-instance-5594_11368"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11369">
                    <BreadcrumbIndicator
                        id="5594_11369"
                        class="Pixso-instance-5594_11369"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11370">
                    <BreadcrumbLinkItem
                        id="5594_11370"
                        class="Pixso-instance-5594_11370"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Subtle"
                    />
                </slot>
                <slot name="slot_5594_11371">
                    <BreadcrumbIndicator
                        id="5594_11371"
                        class="Pixso-instance-5594_11371"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11372">
                    <BreadcrumbLinkItem
                        id="5594_11372"
                        class="Pixso-instance-5594_11372"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Subtle"
                    />
                </slot>
                <slot name="slot_5594_11373">
                    <BreadcrumbIndicator
                        id="5594_11373"
                        class="Pixso-instance-5594_11373"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11374">
                    <BreadcrumbLinkItem
                        id="5594_11374"
                        class="Pixso-instance-5594_11374"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="Subtle"
                    />
                </slot>
            </div>
            <div
                id="5594_11649"
                class="Pixso-symbol-5594_11649"
                v-if="
                    Style === 'Fill' &&
                    IsBoxed === 'False' &&
                    Divider === 'Colon'
                "
            >
                <slot name="slot_5594_11650">
                    <ButtonIcon
                        id="5594_11650"
                        class="Pixso-instance-5594_11650"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11651">
                    <BreadcrumbIndicator
                        id="5594_11651"
                        class="Pixso-instance-5594_11651"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11652">
                    <BreadcrumbLinkItem
                        id="5594_11652"
                        class="Pixso-instance-5594_11652"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Subtle"
                    />
                </slot>
                <slot name="slot_5594_11653">
                    <BreadcrumbIndicator
                        id="5594_11653"
                        class="Pixso-instance-5594_11653"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11654">
                    <BreadcrumbLinkItem
                        id="5594_11654"
                        class="Pixso-instance-5594_11654"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Subtle"
                    />
                </slot>
                <slot name="slot_5594_11655">
                    <BreadcrumbIndicator
                        id="5594_11655"
                        class="Pixso-instance-5594_11655"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11656">
                    <BreadcrumbLinkItem
                        id="5594_11656"
                        class="Pixso-instance-5594_11656"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="Subtle"
                    />
                </slot>
            </div>
            <div
                id="5594_11152"
                class="stroke-wrapper-5594_11152"
                v-if="
                    Style === 'Fill' && IsBoxed === 'True' && Divider === 'Icon'
                "
            >
                <div class="Pixso-symbol-5594_11152">
                    <slot name="slot_5594_11153">
                        <ButtonIcon
                            id="5594_11153"
                            class="Pixso-instance-5594_11153"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11154">
                        <BreadcrumbIndicator
                            id="5594_11154"
                            class="Pixso-instance-5594_11154"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11155">
                        <BreadcrumbLinkItem
                            id="5594_11155"
                            class="Pixso-instance-5594_11155"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Subtle"
                        />
                    </slot>
                    <slot name="slot_5594_11156">
                        <BreadcrumbIndicator
                            id="5594_11156"
                            class="Pixso-instance-5594_11156"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11157">
                        <BreadcrumbLinkItem
                            id="5594_11157"
                            class="Pixso-instance-5594_11157"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Subtle"
                        />
                    </slot>
                    <slot name="slot_5594_11158">
                        <BreadcrumbIndicator
                            id="5594_11158"
                            class="Pixso-instance-5594_11158"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11159">
                        <BreadcrumbLinkItem
                            id="5594_11159"
                            class="Pixso-instance-5594_11159"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="Subtle"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11152 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11375"
                class="stroke-wrapper-5594_11375"
                v-if="
                    Style === 'Fill' &&
                    IsBoxed === 'True' &&
                    Divider === 'Slash'
                "
            >
                <div class="Pixso-symbol-5594_11375">
                    <slot name="slot_5594_11376">
                        <ButtonIcon
                            id="5594_11376"
                            class="Pixso-instance-5594_11376"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11377">
                        <BreadcrumbIndicator
                            id="5594_11377"
                            class="Pixso-instance-5594_11377"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11378">
                        <BreadcrumbLinkItem
                            id="5594_11378"
                            class="Pixso-instance-5594_11378"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Subtle"
                        />
                    </slot>
                    <slot name="slot_5594_11379">
                        <BreadcrumbIndicator
                            id="5594_11379"
                            class="Pixso-instance-5594_11379"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11380">
                        <BreadcrumbLinkItem
                            id="5594_11380"
                            class="Pixso-instance-5594_11380"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Subtle"
                        />
                    </slot>
                    <slot name="slot_5594_11381">
                        <BreadcrumbIndicator
                            id="5594_11381"
                            class="Pixso-instance-5594_11381"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11382">
                        <BreadcrumbLinkItem
                            id="5594_11382"
                            class="Pixso-instance-5594_11382"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="Subtle"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11375 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11657"
                class="stroke-wrapper-5594_11657"
                v-if="
                    Style === 'Fill' &&
                    IsBoxed === 'True' &&
                    Divider === 'Colon'
                "
            >
                <div class="Pixso-symbol-5594_11657">
                    <slot name="slot_5594_11658">
                        <ButtonIcon
                            id="5594_11658"
                            class="Pixso-instance-5594_11658"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11659">
                        <BreadcrumbIndicator
                            id="5594_11659"
                            class="Pixso-instance-5594_11659"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11660">
                        <BreadcrumbLinkItem
                            id="5594_11660"
                            class="Pixso-instance-5594_11660"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Subtle"
                        />
                    </slot>
                    <slot name="slot_5594_11661">
                        <BreadcrumbIndicator
                            id="5594_11661"
                            class="Pixso-instance-5594_11661"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11662">
                        <BreadcrumbLinkItem
                            id="5594_11662"
                            class="Pixso-instance-5594_11662"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Subtle"
                        />
                    </slot>
                    <slot name="slot_5594_11663">
                        <BreadcrumbIndicator
                            id="5594_11663"
                            class="Pixso-instance-5594_11663"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11664">
                        <BreadcrumbLinkItem
                            id="5594_11664"
                            class="Pixso-instance-5594_11664"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="Subtle"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11657 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11044"
                class="Pixso-symbol-5594_11044"
                v-if="
                    Style === 'Outlined' &&
                    IsBoxed === 'False' &&
                    Divider === 'Icon'
                "
            >
                <slot name="slot_5594_11045">
                    <ButtonIcon
                        id="5594_11045"
                        class="Pixso-instance-5594_11045"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11046">
                    <BreadcrumbIndicator
                        id="5594_11046"
                        class="Pixso-instance-5594_11046"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_11047">
                    <BreadcrumbLinkItem
                        id="5594_11047"
                        class="Pixso-instance-5594_11047"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Outlined"
                    />
                </slot>
                <slot name="slot_5594_11048">
                    <BreadcrumbIndicator
                        id="5594_11048"
                        class="Pixso-instance-5594_11048"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_11049">
                    <BreadcrumbLinkItem
                        id="5594_11049"
                        class="Pixso-instance-5594_11049"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Outlined"
                    />
                </slot>
                <slot name="slot_5594_11050">
                    <BreadcrumbIndicator
                        id="5594_11050"
                        class="Pixso-instance-5594_11050"
                        DividerType="Icon"
                    />
                </slot>
                <slot name="slot_5594_11051">
                    <BreadcrumbLinkItem
                        id="5594_11051"
                        class="Pixso-instance-5594_11051"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="Outlined"
                    />
                </slot>
            </div>
            <div
                id="5594_11383"
                class="Pixso-symbol-5594_11383"
                v-if="
                    Style === 'Outlined' &&
                    IsBoxed === 'False' &&
                    Divider === 'Slash'
                "
            >
                <slot name="slot_5594_11384">
                    <ButtonIcon
                        id="5594_11384"
                        class="Pixso-instance-5594_11384"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11385">
                    <BreadcrumbIndicator
                        id="5594_11385"
                        class="Pixso-instance-5594_11385"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11386">
                    <BreadcrumbLinkItem
                        id="5594_11386"
                        class="Pixso-instance-5594_11386"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Outlined"
                    />
                </slot>
                <slot name="slot_5594_11387">
                    <BreadcrumbIndicator
                        id="5594_11387"
                        class="Pixso-instance-5594_11387"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11388">
                    <BreadcrumbLinkItem
                        id="5594_11388"
                        class="Pixso-instance-5594_11388"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Outlined"
                    />
                </slot>
                <slot name="slot_5594_11389">
                    <BreadcrumbIndicator
                        id="5594_11389"
                        class="Pixso-instance-5594_11389"
                        DividerType="Slash"
                    />
                </slot>
                <slot name="slot_5594_11390">
                    <BreadcrumbLinkItem
                        id="5594_11390"
                        class="Pixso-instance-5594_11390"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="Outlined"
                    />
                </slot>
            </div>
            <div
                id="5594_11665"
                class="Pixso-symbol-5594_11665"
                v-if="
                    Style === 'Outlined' &&
                    IsBoxed === 'False' &&
                    Divider === 'Colon'
                "
            >
                <slot name="slot_5594_11666">
                    <ButtonIcon
                        id="5594_11666"
                        class="Pixso-instance-5594_11666"
                        Hierarchy="No Fill"
                        Size="sm"
                        Color="Gray"
                        State="Default"
                    >
                        <template #slot_5590_22156>
                            <HouseSimple
                                id="5590_22156"
                                class="Pixso-instance-5590_22156"
                            />
                        </template>
                    </ButtonIcon>
                </slot>
                <slot name="slot_5594_11667">
                    <BreadcrumbIndicator
                        id="5594_11667"
                        class="Pixso-instance-5594_11667"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11668">
                    <BreadcrumbLinkItem
                        id="5594_11668"
                        class="Pixso-instance-5594_11668"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Outlined"
                    />
                </slot>
                <slot name="slot_5594_11669">
                    <BreadcrumbIndicator
                        id="5594_11669"
                        class="Pixso-instance-5594_11669"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11670">
                    <BreadcrumbLinkItem
                        id="5594_11670"
                        class="Pixso-instance-5594_11670"
                        :visible_5594_0="false"
                        State="Default"
                        Fill="Outlined"
                    />
                </slot>
                <slot name="slot_5594_11671">
                    <BreadcrumbIndicator
                        id="5594_11671"
                        class="Pixso-instance-5594_11671"
                        DividerType="Colon"
                    />
                </slot>
                <slot name="slot_5594_11672">
                    <BreadcrumbLinkItem
                        id="5594_11672"
                        class="Pixso-instance-5594_11672"
                        :visible_5594_0="false"
                        State="Active"
                        Fill="Outlined"
                    />
                </slot>
            </div>
            <div
                id="5594_11160"
                class="stroke-wrapper-5594_11160"
                v-if="
                    Style === 'Outlined' &&
                    IsBoxed === 'True' &&
                    Divider === 'Icon'
                "
            >
                <div class="Pixso-symbol-5594_11160">
                    <slot name="slot_5594_11161">
                        <ButtonIcon
                            id="5594_11161"
                            class="Pixso-instance-5594_11161"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11162">
                        <BreadcrumbIndicator
                            id="5594_11162"
                            class="Pixso-instance-5594_11162"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11163">
                        <BreadcrumbLinkItem
                            id="5594_11163"
                            class="Pixso-instance-5594_11163"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Outlined"
                        />
                    </slot>
                    <slot name="slot_5594_11164">
                        <BreadcrumbIndicator
                            id="5594_11164"
                            class="Pixso-instance-5594_11164"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11165">
                        <BreadcrumbLinkItem
                            id="5594_11165"
                            class="Pixso-instance-5594_11165"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Outlined"
                        />
                    </slot>
                    <slot name="slot_5594_11166">
                        <BreadcrumbIndicator
                            id="5594_11166"
                            class="Pixso-instance-5594_11166"
                            DividerType="Icon"
                        />
                    </slot>
                    <slot name="slot_5594_11167">
                        <BreadcrumbLinkItem
                            id="5594_11167"
                            class="Pixso-instance-5594_11167"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="Outlined"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11160 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11391"
                class="stroke-wrapper-5594_11391"
                v-if="
                    Style === 'Outlined' &&
                    IsBoxed === 'True' &&
                    Divider === 'Slash'
                "
            >
                <div class="Pixso-symbol-5594_11391">
                    <slot name="slot_5594_11392">
                        <ButtonIcon
                            id="5594_11392"
                            class="Pixso-instance-5594_11392"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11393">
                        <BreadcrumbIndicator
                            id="5594_11393"
                            class="Pixso-instance-5594_11393"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11394">
                        <BreadcrumbLinkItem
                            id="5594_11394"
                            class="Pixso-instance-5594_11394"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Outlined"
                        />
                    </slot>
                    <slot name="slot_5594_11395">
                        <BreadcrumbIndicator
                            id="5594_11395"
                            class="Pixso-instance-5594_11395"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11396">
                        <BreadcrumbLinkItem
                            id="5594_11396"
                            class="Pixso-instance-5594_11396"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Outlined"
                        />
                    </slot>
                    <slot name="slot_5594_11397">
                        <BreadcrumbIndicator
                            id="5594_11397"
                            class="Pixso-instance-5594_11397"
                            DividerType="Slash"
                        />
                    </slot>
                    <slot name="slot_5594_11398">
                        <BreadcrumbLinkItem
                            id="5594_11398"
                            class="Pixso-instance-5594_11398"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="Outlined"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11391 stroke-gray30-35_1481"></div>
            </div>
            <div
                id="5594_11673"
                class="stroke-wrapper-5594_11673"
                v-if="
                    Style === 'Outlined' &&
                    IsBoxed === 'True' &&
                    Divider === 'Colon'
                "
            >
                <div class="Pixso-symbol-5594_11673">
                    <slot name="slot_5594_11674">
                        <ButtonIcon
                            id="5594_11674"
                            class="Pixso-instance-5594_11674"
                            Hierarchy="No Fill"
                            Size="sm"
                            Color="Gray"
                            State="Default"
                        >
                            <template #slot_5590_22156>
                                <HouseSimple
                                    id="5590_22156"
                                    class="Pixso-instance-5590_22156"
                                />
                            </template>
                        </ButtonIcon>
                    </slot>
                    <slot name="slot_5594_11675">
                        <BreadcrumbIndicator
                            id="5594_11675"
                            class="Pixso-instance-5594_11675"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11676">
                        <BreadcrumbLinkItem
                            id="5594_11676"
                            class="Pixso-instance-5594_11676"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Outlined"
                        />
                    </slot>
                    <slot name="slot_5594_11677">
                        <BreadcrumbIndicator
                            id="5594_11677"
                            class="Pixso-instance-5594_11677"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11678">
                        <BreadcrumbLinkItem
                            id="5594_11678"
                            class="Pixso-instance-5594_11678"
                            :visible_5594_0="false"
                            State="Default"
                            Fill="Outlined"
                        />
                    </slot>
                    <slot name="slot_5594_11679">
                        <BreadcrumbIndicator
                            id="5594_11679"
                            class="Pixso-instance-5594_11679"
                            DividerType="Colon"
                        />
                    </slot>
                    <slot name="slot_5594_11680">
                        <BreadcrumbLinkItem
                            id="5594_11680"
                            class="Pixso-instance-5594_11680"
                            :visible_5594_0="false"
                            State="Active"
                            Fill="Outlined"
                        />
                    </slot>
                </div>
                <div class="stroke-5594_11673 stroke-gray30-35_1481"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import ButtonIcon from "@/components/Buttonicon.vue";
import HouseSimple from "@/components/Housesimple.vue";
import BreadcrumbIndicator from "@/components/Breadcrumbindicator.vue";
import BreadcrumbLinkItem from "@/components/Breadcrumblinkitem.vue";
const props = defineProps({
    Style: { type: String },
    IsBoxed: { type: String },
    Divider: { type: String }
});
</script>
<style>
.Pixso-symbol-5594_10959 {
}
.Pixso-symbol-5594_10952 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_10902 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5590_22156 {
    width: undefinedpx;
    height: undefinedpx;
}
.Pixso-instance-5594_10926 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10874 {
    width: 61px;
    height: 20px;
}
.Pixso-paragraph-5522_33761 {
    text-align: center;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    width: auto;
    height: auto;
    flex-grow: 0;
}
.Pixso-instance-5594_10912 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10915 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_10921 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10918 {
    width: 61px;
    height: 20px;
}
.Pixso-symbol-5594_11351 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11352 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11353 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11354 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11355 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11356 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11357 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11358 {
    width: 61px;
    height: 20px;
}
.Pixso-symbol-5594_11633 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11634 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11635 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11636 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11637 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11638 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11639 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11640 {
    width: 61px;
    height: 20px;
}
.Pixso-symbol-5594_11144 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11144 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11144 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11145 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11146 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11147 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11148 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11149 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11150 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11151 {
    width: 61px;
    height: 20px;
}
.Pixso-symbol-5594_11359 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11359 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11359 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11360 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11361 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11362 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11363 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11364 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11365 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11366 {
    width: 61px;
    height: 20px;
}
.Pixso-symbol-5594_11641 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11641 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11641 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11642 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11643 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11644 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11645 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11646 {
    width: 61px;
    height: 20px;
}
.Pixso-instance-5594_11647 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11648 {
    width: 61px;
    height: 20px;
}
.Pixso-symbol-5594_10988 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_10989 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_10990 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10991 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_10992 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10993 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_10994 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10995 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11367 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11368 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11369 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11370 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11371 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11372 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11373 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11374 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11649 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11650 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11651 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11652 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11653 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11654 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11655 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11656 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11152 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11152 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11152 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11153 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11154 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11155 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11156 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11157 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11158 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11159 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11375 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11375 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11375 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11376 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11377 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11378 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11379 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11380 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11381 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11382 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11657 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11657 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11657 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11658 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11659 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11660 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11661 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11662 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11663 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11664 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11044 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11045 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11046 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11047 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11048 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11049 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11050 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11051 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11383 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11384 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11385 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11386 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11387 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11388 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11389 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11390 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11665 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5594_11666 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11667 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11668 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11669 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11670 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11671 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11672 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11160 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11160 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11160 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11161 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11162 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11163 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11164 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11165 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11166 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11167 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11391 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11391 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11391 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11392 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11393 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11394 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11395 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11396 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11397 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11398 {
    width: 77px;
    height: 32px;
}
.Pixso-symbol-5594_11673 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    padding: 12px 12px 12px 12px;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5594_11673 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-5594_11673 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11674 {
    width: 32px;
    height: 32px;
}
.Pixso-instance-5594_11675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11676 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11677 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11678 {
    width: 77px;
    height: 32px;
}
.Pixso-instance-5594_11679 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11680 {
    width: 77px;
    height: 32px;
}

.Pixso-instance-5594_10902 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5590_22156 .Pixso-instance-5590_22156 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10926 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_10874 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10874 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_10874 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_10912 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_10915 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10915 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_10915 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_10921 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_10918 .Pixso-symbol-5594_6708 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_10918 .Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10918 .Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11352 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11353 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11354 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11354 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11354 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11355 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11356 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11356 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11356 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11357 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11358 .Pixso-symbol-5594_6708 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11358 .Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11358 .Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11634 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11635 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11636 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11636 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11636 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11637 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11638 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11638 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11638 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11639 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11640 .Pixso-symbol-5594_6708 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11640 .Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11640 .Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11145 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11146 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11147 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11147 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11147 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11148 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11149 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11149 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11149 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11150 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11151 .Pixso-symbol-5594_6708 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11151 .Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11151 .Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11360 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11361 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11362 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11362 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11362 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11363 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11364 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11364 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11364 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11365 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11366 .Pixso-symbol-5594_6708 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11366 .Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11366 .Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11642 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11643 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11644 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11644 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11644 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11645 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11646 .Pixso-instance-5522_33739 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11646 .Pixso-paragraph-5522_33761 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11646 .Pixso-symbol-5522_33763 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11647 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11648 .Pixso-symbol-5594_6708 {
    width: 61px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
}
.Pixso-instance-5594_11648 .Pixso-instance-5594_6709 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11648 .Pixso-paragraph-5594_6710 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_10989 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_10990 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_10991 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_10991 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10991 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_10992 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_10993 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_10993 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10993 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_10994 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_10995 .Pixso-symbol-5594_6732 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_10995 .Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_10995 .Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11368 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11369 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11370 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11370 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11370 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11371 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11372 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11372 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11372 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11373 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11374 .Pixso-symbol-5594_6732 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11374 .Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11374 .Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11650 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11651 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11652 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11652 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11652 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11653 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11654 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11654 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11654 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11655 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11656 .Pixso-symbol-5594_6732 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11656 .Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11656 .Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11153 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11154 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11155 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11155 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11155 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11156 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11157 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11157 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11157 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11158 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11159 .Pixso-symbol-5594_6732 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11159 .Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11159 .Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11376 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11377 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11378 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11378 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11378 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11379 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11380 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11380 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11380 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11381 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11382 .Pixso-symbol-5594_6732 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11382 .Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11382 .Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11658 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11659 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11660 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11660 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11660 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11661 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11662 .Pixso-symbol-5594_6674 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11662 .Pixso-instance-5594_6675 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11662 .Pixso-paragraph-5594_6676 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11663 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11664 .Pixso-symbol-5594_6732 {
    width: 77px;
    height: 32px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11664 .Pixso-instance-5594_6733 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11664 .Pixso-paragraph-5594_6734 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11045 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11046 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11047 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11047 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11047 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11047 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11047 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11048 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11049 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11049 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11049 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11049 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11049 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11050 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11051 .Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11051 .stroke-wrapper-5594_6756 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11051 .stroke-5594_6756 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11051 .Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11051 .Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11384 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11385 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11386 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11386 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11386 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11386 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11386 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11387 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11388 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11388 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11388 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11388 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11388 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11389 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11390 .Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11390 .stroke-wrapper-5594_6756 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11390 .stroke-5594_6756 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11390 .Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11390 .Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11666 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11667 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11668 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11668 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11668 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11668 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11668 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11669 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11670 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11670 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11670 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11670 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11670 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11671 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11672 .Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11672 .stroke-wrapper-5594_6756 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11672 .stroke-5594_6756 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11672 .Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11672 .Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11161 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11162 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11163 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11163 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11163 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11163 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11163 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11164 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11165 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11165 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11165 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11165 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11165 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11166 .Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-5594_11167 .Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11167 .stroke-wrapper-5594_6756 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11167 .stroke-5594_6756 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11167 .Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11167 .Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11392 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11393 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11394 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11394 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11394 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11394 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11394 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11395 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11396 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11396 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11396 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11396 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11396 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11397 .Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11398 .Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11398 .stroke-wrapper-5594_6756 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11398 .stroke-5594_6756 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11398 .Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11398 .Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11674 .Pixso-symbol-5590_22155 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 16px 16px 16px 16px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11675 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11676 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11676 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11676 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11676 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11676 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11677 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11678 .Pixso-symbol-5594_6682 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11678 .stroke-wrapper-5594_6682 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11678 .stroke-5594_6682 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11678 .Pixso-instance-5594_6683 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11678 .Pixso-paragraph-5594_6684 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_11679 .Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-instance-5594_11680 .Pixso-symbol-5594_6756 {
    width: 100%;
    height: 100%;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 4px;
    align-items: center;
    padding: 6px 8px 6px 8px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5594_11680 .stroke-wrapper-5594_6756 {
    width: 77px;
    height: 32px;
    display: flex;
    flex-shrink: 0;
}
.Pixso-instance-5594_11680 .stroke-5594_6756 {
    inset: 0px;
    border-radius: 123px 123px 123px 123px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5594_11680 .Pixso-instance-5594_6757 {
    width: 20px;
    height: 20px;
}
.Pixso-instance-5594_11680 .Pixso-paragraph-5594_6758 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-instance-5594_10902 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11352 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11634 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11145 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11360 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11642 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_10989 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11368 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11650 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11153 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11376 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11658 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11045 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11384 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11666 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11161 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11392 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_11674 .Pixso-instance-5590_22156 .Pixso-symbol-6041_60589 {
    width: 20px;
    height: 20px;
    position: absolute;
    left: 52px;
    top: 12px;
    background-color: transparent;
}
.Pixso-instance-5594_10902 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11352 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11634 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11145 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11360 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11642 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_10989 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11368 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11650 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11153 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11376 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11658 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11045 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11384 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11666 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11161 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11392 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
.Pixso-instance-5594_11674 .Pixso-instance-5590_22156 .Pixso-vector-6041_60590 {
    width: 65.11%;
    height: 67.71%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.11%;
    right: 25.78%;
    top: 6.51%;
    bottom: 25.78%;
}
</style>
