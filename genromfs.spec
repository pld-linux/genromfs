Summary:	Utility for creating romfs filesystems
Summary(pl.UTF-8):	Narzędzie do tworzenia systemów plików romfs
Name:		genromfs
Version:	0.5.2
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/romfs/%{name}-%{version}.tar.gz
# Source0-md5:	2a91463c56f9e042edc330c063a0cf5a
Patch0:		%{name}-ac_am.patch
URL:		http://romfs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux kernel.
Romfs filesystems are mainly used for the initial RAM disks used
during installation.

%description -l pl.UTF-8
genromfs jest narzędziem służącym do tworzenia systemów plików romfs,
które są lekkimi systemami plików tylko do odczytu, obsługiwanymi
przez jądro Linuksa. Romfs jest głównie używany na inicjalnym
ramdysku, używanym w trakcie startu systemu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS genromfs.lsm romfs.txt
%attr(755,root,root) %{_sbindir}/genromfs
%{_mandir}/man8/genromfs.8*
