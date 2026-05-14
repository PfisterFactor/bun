%global debug_package %{nil}
%global __os_install_post %{nil}
%global _build_id_links none

Name:           bun
Version:        %{_version}
Release:        0.%{_buildnum}.git%{_shortsha}%{?dist}
Summary:        JavaScript runtime, bundler, transpiler, and package manager
License:        MIT
URL:            https://github.com/%{_owner}/bun
ExclusiveArch:  x86_64 aarch64

Source0:        bun
Source1:        LICENSE.md

%description
Bun is a fast all-in-one JavaScript runtime. It bundles TypeScript, JSX, and
modern JavaScript; runs tests; manages packages; and serves as a drop-in
Node.js replacement.

All major dependencies (JavaScriptCore, BoringSSL, zlib-ng, libarchive, etc.)
are statically linked.

%prep

%build

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/bun
install -D -m 0644 %{SOURCE1} %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.md

%files
%license %{_defaultlicensedir}/%{name}/LICENSE.md
%{_bindir}/bun

%changelog
* %{_changelog_date} PfisterFactor <eric.pfister@example.com> - %{version}-%{release}
- Automated build from commit %{_shortsha}
