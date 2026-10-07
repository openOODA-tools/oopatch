Name:           oopatch
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-bounded unified diff applier with fuzz factor and reverse rollback.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oopatch
Source0:        oopatch-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oopatch is a sovereign, capability-bounded PATCH APPLIER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oopatch
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oopatch-uninstall

%files
/usr/bin/oopatch
/usr/bin/oopatch-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
