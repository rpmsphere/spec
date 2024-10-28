Name:           vimmate
Version:        0.6.6
Release:        14.1
Source:         VimMate-0.6.6.tar.bz2
License:        GPL
Group:          Productivity/Editors/VimMate 
BuildArch:      noarch
BuildRequires:  vim gvim ruby rubygems
Requires:       vim gvim ruby rubygem-gtk2
Summary:        VimMate
URL:            https://vimmate.rubyforge.org/ 

%description
VimMate is a graphical add-on to Vim with IDE-like features: it does more than 
the plain Vim while still being lightweight. Even with the additional features, 
it stays out of the way for it‘s main task: editing files with Vim. VimMate adds 
functionality to Vim by embedding Vim GTK GUI (gVim) within VimMate. 

%prep
%setup -q -n VimMate-%{version} 

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__mkdir} -p $RPM_BUILD_ROOT/%{_datadir}/ruby
%{__cp} ./bin/vimmate $RPM_BUILD_ROOT/%{_bindir}
%{__cp} -r ./lib/vimmatelib* $RPM_BUILD_ROOT/%{_datadir}/ruby

%files
%doc README TODO
%{_bindir}/vimmate
%{_datadir}/ruby/*

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.6
- Rebuilt for Fedora
* Mon May 17 2010 - Matthias Weckbecker <mweckbecker@suse.de>
- library patch for vimmatelib fixed                            
* Fri Sep 04 2009 - mweckbecker@suse.de
- added symlink to vimmate's library
- fixed header in spec file
* Thu Sep 03 2009 - mweckbecker@suse.de
- initial package with version 0.6.6 
