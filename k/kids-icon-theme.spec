%define theme_name Kids

Summary: %{theme_name} icon theme
Name: kids-icon-theme
Version: 1.1
Release: 6.1
License: GPL
Group: User Interface/Desktops
Source0: kids.tgz
BuildArch: noarch

%description
%{theme_name} icon theme 0.1+1.0
with wallpaper by Andreas Ochs.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a index.theme *x* %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Sep 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Wed May 23 2007 - aochs@gmx.de
- changed wallpaper 
* Fri Apr 13 2007 - l.rupp@web.de
- use the original sources(!)
- updated kids.xml
- use wallpaper from kde-look
* Tue Apr 10 2007 - aochs@gmx.de
- initial package 1.0
-  contains icons from Icon Theme by Everaldo Coelho
   www.yellowicon.com
   www.everaldo.com
   everaldo@everaldo.com
