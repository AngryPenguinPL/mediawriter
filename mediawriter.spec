%define oname MediaWriter

Name:           mediawriter
Version:        4.1.2
Release:        1
Summary:        Fedora Media Writer

License:        GPLv2+
URL:            https://github.com/FedoraQt/MediaWriter
Source0:        https://github.com/FedoraQt/MediaWriter/archive/%{version}/%{oname}-%{version}.tar.gz

Provides:       liveusb-creator = %{version}-%{release}
Obsoletes:      liveusb-creator <= 3.95.4-2

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative
BuildRequires:  gettext
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)

#Requires:       qt5-qtbase
Requires:       qt5-qtquickcontrols >= 5.3.0
Requires:       polkit
Requires:       xz
#Requires: storaged
Requires: udisks



%description
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.

%prep
%setup -q -n %{oname}-%{version}
mkdir %{_target_platform}

%build
pushd %{_target_platform}
%{qmake_qt5} PREFIX=%{_prefix} MEDIAWRITER_VERSION=%{version}-%{release} ..
popd
%make_build -C %{_target_platform}

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

#No check (penguin)
#check
#appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png


%changelog
* Thu Aug 02 2018 Martin Bříza <m@rtinbriza.cz> - 4.1.2-1
- Update to 4.1.2
- Update URLs
- Resolves #1590315

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.1-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Martin Bříza <mbriza@redhat.com> 4.1.1-1
- Update to 4.1.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Martin Bříza <mbriza@redhat.com> 4.1.0-1
- Update to 4.1.0
- Depend on UDisks2 instead of storage if Fedora != 25

* Tue Apr 11 2017 Martin Bříza <mbriza@redhat.com> 4.0.95-2
- Get rid of {?_isa} in the dependencies 

* Mon Mar 20 2017 Martin Bříza <mbriza@redhat.com> 4.0.95-1
- Update to 4.0.95

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Martin Bříza <mbriza@redhat.com> 4.0.8-0
- Update to 4.0.8

* Tue Nov 22 2016 Martin Bříza <mbriza@redhat.com> 4.0.7-0
- Update to 4.0.7

* Mon Nov 21 2016 Martin Bříza <mbriza@redhat.com> 4.0.5-0
- Update to 4.0.5

* Fri Nov 11 2016 Martin Bříza <mbriza@redhat.com> 4.0.4-0
- Update to 4.0.4

* Wed Nov 02 2016 Martin Bříza <mbriza@redhat.com> 4.0.3-0
- Update to 4.0.2

* Wed Nov 02 2016 Martin Bříza <mbriza@redhat.com> 4.0.1-0
- Update to 4.0.1

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-2
- Don't forget to update the icon cache

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-1
- Make mediawriter obsolete the liveusb-creator package

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-0
- Update to 4.0.0

* Tue Oct 11 2016 Martin Bříza <mbriza@redhat.com> 3.97.2-0
- Update to 3.97.2

* Fri Sep 23 2016 Martin Bříza <mbriza@redhat.com> 3.97.1-0
- Update to 3.97.1

* Thu Sep 22 2016 Martin Bříza <mbriza@redhat.com> 3.97.0-0
- Update to 3.97.0

* Fri Sep 16 2016 Martin Bříza <mbriza@redhat.com> 3.96.0-0
- Update to 3.96.0

* Wed Aug 10 2016 Martin Bříza <mbriza@redhat.com> 0-1.1git728a879
- Fixed MOC errors when compiling on F25 and above

* Tue Aug 9 2016 Martin Bříza <mbriza@redhat.com> 0-0.2git0049ab3
- Fixed a package name

* Tue Aug 9 2016 Martin Bříza <mbriza@redhat.com> 0-0.1git0049ab3
- Initial release
