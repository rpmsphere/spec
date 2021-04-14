Summary: Chat application written in C for the GTK+ toolkit
Name: vqcc-gtk
Version: 0.5
Release: 5.1
License: GPL
Group: Applications/Communications
Source: http://sourceforge.net/projects/vqcc-gtk/files/%{name}/%{version}/%{name}-%{version}.tar.gz
URL: http://vqcc-gtk.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: gtk2-devel

%description
Vqcc-gtk is a chat application written in C for the GTK+ toolkit
by Saulius Menkevicius <razzmatazz@mail.lt>.
Primarily used in small LAN, based on quickChat/VypressChat 
for Windows (from Vypress Research) and is licensed under the GPL.

%prep
%setup -q

%build
export LDFLAGS=-lX11
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/vqcc-gtk
%{_datadir}/locale/*/LC_MESSAGES/vqcc-gtk.mo
%{_datadir}/applications/vqcc-gtk.desktop
%{_datadir}/pixmaps/vqcc-gtk.png

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Wed Aug 31 2004 Vilius Roskus <soling@navigator.lv> v0.4.1
- a really ugly bug where text could not get entered into the text box at the bottom fixed (thanks mustafaogun);
* Fri Aug 27 2004 Vilius Roskus <soling@navigator.lv> v0.4
- popups network detection/configuration dialog on first startup and in cases when network error occurs;
- shows IP address on user info tooltip;
- uses startup notification to notify desktop environment when startup is complete;
- application shortcut & icon is copied to appropriate places during installation;
- fixed a bug where vqcc-gtk segfaulted when showing preferences dialog (thanks Cass Evert);
- user list can be refreshed via it's popup menu; unreplied users can get removed too;
- dead users can be removed from the list with the help of context menu;
- network charset encoding can be selected from the list (when GTK+ is 2.4+) */
- user of the application gets shown on the user list too;
- added "invisible" user mode (suppresses replies to refresh requests; hides user when joining/leaving a channel);
- added support for persistent channels (a checkbox in "Channel list" dialog);
- shows the main vqcc-gtk window if the systray icon could not get shown on notification area or the area had disappeared;
- page text is now wrapped on character basis;
- increased max topic and message length to 1023 chars;
- an option to block mass messages was added;
- "Quote" button has been added to the message dialog;
- various bugfixes and refinements;
