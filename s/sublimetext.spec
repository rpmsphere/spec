%global debug_package %{nil}

Name: sublimetext
Summary: A sophisticated text editor for code, markup and prose
Version: 3
Release: 0.3059.bin
License: freeware
Group: Development/Tools
Source0: %{name}.desktop
Source1: http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3059_x32.tar.bz2
Source2: http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3059_x64.tar.bz2
URL: http://www.sublimetext.com/

%description
You'll love the slick user interface, extraordinary features and amazing performance.

%prep
%ifarch x86_64
%setup -q -T -b 2 -n sublime_text_3
%else
%setup -q -T -b 1 -n sublime_text_3
%endif

%build

%install
%__mkdir_p %{buildroot}%{_libexecdir}/%{name}
%__cp -a * %{buildroot}%{_libexecdir}/%{name}
install -Dm644 %{SOURCE0} %{buildroot}%{_libexecdir}/applications/%{name}.desktop
%__mkdir_p %{buildroot}%{_bindir}
ln -s ../libexec/%{name}/sublime_text %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_libexecdir}/applications/%{name}.desktop
%{_libexecdir}/%{name}

%changelog
* Thu Feb 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 3
- Inital binary package
