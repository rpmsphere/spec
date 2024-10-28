%undefine _debugsource_packages

Summary:        OXIM filter packs
Name:           oxim-filters
Version:        0.4
Release:        3
License:        GPLv2+
Group:          User Interface/Desktops
Source0:        %{name}-%{version}.tar.gz
URL:            https://github.com/chinese-opendesktop/oxim-filters
#BuildArch:     noarch
Requires:       oxim >= 1.4.0

%description
The OXIM filters are some useful tools for oxim to 
help user to input chinese words.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
bindir=%{_bindir} libdir=%{_libdir} DESTDIR=%{buildroot} make install

%files
%{_libdir}/oxim/filters/*

%changelog
* Wed Mar 27 2013 Robert Wei <robert.wei@ossii.com.tw> 0.4-2
- Add paste filter.
* Tue Feb 05 2013 Robert Wei <robert.wei@ossii.com.tw> 0.4-1
- Add zhottp speak interface.
* Wed Sep 15 2010 Chih-Chun Tu <vincent.tu@ossii.com.tw> 0.3-2
- Add oxim_typing filter module.
* Tue Aug 10 2010 Wei-Lun Chao <bluebat@member.fsf.org> 0.3-1
- Move some executables to zhotools.
* Fri Apr 30 2010 Wind <yc.yan@ossii.com.tw> 0.2-2
- Build for new version.
* Thu Apr 22 2010 Wind <yc.yan@ossii.com.tw> 0.2-1
- Build for new version.
* Wed Sep 23 2009 Wind <yc.yan@ossii.com.tw> 0.1
- Build for OSSII.
