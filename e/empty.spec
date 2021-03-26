Name:    empty
Version: 0.6.11b
Release: 1
Summary: Run interactive console applications in batch mode
Summary(ru_RU): Запуск интерактивных консольных приложений в автоматическом режиме
Summary(zh_TW): 在批次模式中執行互動式終端機應用軟體
License: Common Public License
Group:   System/Configuration
URL:     http://%name.sourceforge.net
Source:  http://heanet.dl.sourceforge.net/sourceforge/%name/%name-%version.tgz

%description
empty is an utility that provides an interface to execute and/or interact
with processes under pseudo-terminal sessions (PTYs). This tool is definitely
useful in programming of shell scripts designed to communicate with interactive
programs like telnet, ssh, ftp, etc. In some cases empty can be the simplest
replacement for TCL/expect or other similar programming tools because empty:

    * can be easily invoked directly from shell prompt or script
    * does not use TCL, Perl, PHP, Python,... as an underlying language
    * is written entirely in C
    * has small and simple source code
    * can easily be ported to almost all UNIX-like systems

%description -l ru_RU
Empty - это утилита, которая служит для организации автоматического выполнения
интерактивных консольных приложений, таких как telnet, SSH, FTP и т.д.
Для этого Empty создаёт т.н. псевдотерминальную сессию (PTY),
в которой перехватывает вывод приложения на экран и чтение с клавиатуры.
Затем Empty дожидается вывода от приложения заданных пользователем строк
и отправляет приложению назначенные ответы.

Преимущества Empty перед более известными средствами наподобие TCL/Expect:
    * может быть легко вызвана прямо из командной строки или пакетного сценария
    * не требует для работы TCL, Perl, PHP, Python и прочих монстров
    * написана целиком на Си, имеет небольшой и ясный код
    * легко переносима на любые Юникс-подобные системы
В каталоге документации находятся примеры для запуска различных приложений.

%prep
%setup -q

%build
%__cc %optflags -o %name %name.c -lutil

%install
%__mkdir_p %buildroot{%_bindir,%_mandir/man1}
%__cp -a empty   %buildroot%_bindir/
%__cp -a empty.1 %buildroot%_mandir/man1/

%files
%doc README CHANGELOG examples
%_bindir/%name
%_mandir/man1/%name.1.*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.11b
- Rebuild for Fedora
* Thu Jan 18 2007 Ilya Evseev <evseev@altlinux.ru> 0.6.11b-alt1
- update to new version 0.6.11
* Wed Mar 22 2006 Ilya Evseev <evseev@altlinux.ru> 0.6.9b-alt1
- update to new version 0.6.9
* Mon Feb 20 2006 Ilya Evseev <evseev@altlinux.ru> 0.6.8b-alt1
- update to new version 0.6.8
* Tue Dec 20 2005 Ilya Evseev <evseev@altlinux.ru> 0.6.5b-alt1
- update to new version 0.6.5
* Tue Sep 20 2005 Ilya Evseev <evseev@altlinux.ru> 0.6.0b-alt1
- Initial build for ALTLinux
