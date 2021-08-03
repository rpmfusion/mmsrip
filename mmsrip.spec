Summary: MMS Streams Recorder
Name: mmsrip
Version: 0.7.0
Release: 16%{?dist}
License: GPLv2+
URL: http://nbenoit.tuxfamily.org/projects.php?rq=mmsrip
Source: http://nbenoit.tuxfamily.org/projects/mmsrip/%{name}-%{version}.tar.gz
BuildRequires: gcc

%description
MMSRIP is a pure useless program which allows you to save on your hard-disk
the content being streamed by an MMS server. This program has been written
for personnal use, so don't blame me if you think I am stupid doing such
tool for the others.


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/mmsrip
%{_mandir}/man?/*


%changelog
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
- Fix make command
- Add BuildRequires: gcc
- Spec file clean up

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.0-5
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.0-3
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.7.0-2
- rebuild for RPM Fusion

* Fri Sep  8 2006 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Update to 0.7.0.

* Sat Jan 14 2006 Federico Simoncelli <federico.simoncelli@gmail.com>
- Initial release

