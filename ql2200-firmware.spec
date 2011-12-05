Name:		ql2200-firmware
Summary: 	Firmware for qlogic 2200 devices
Version:	2.02.08
Release:	3.1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/ql2200_fw.bin
Source1:	ftp://ftp.qlogic.com/outgoing/linux/firmware/LICENSE
URL:		ftp://ftp.qlogic.com/outgoing/linux/firmware/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Firmware for qlogic 2200 devices.

%prep
%setup -n %{name} -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
# Firmware, do nothing.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware/
install -m0644 ql2200_fw.bin $RPM_BUILD_ROOT/lib/firmware/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
/lib/firmware/ql2200_fw.bin

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.02.08-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.02.08-1
- Initial package for Fedora
