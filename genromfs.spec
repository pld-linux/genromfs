Summary:	Utility for creating romfs filesystems
Name:		genromfs
Version:	0.3
Release:	8
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.banki.hu/pub/linux/local/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux

%define		_sbindir	/sbin

%description
enromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux kernel.
Romfs filesystems are mainly used for the initial RAM disks used
during installation.

%description -l pl
genromfs jest narz�dziem s�u��cym do tworzenia system�w plik�w romfs,
kt�re s� lekkimi systemami plik�w tylko do odczytu, obs�ugiwanymi
przez j�dro Linukxa. Romfs ejst g��wnie u�ywany na inicjalnym ramdysku
kt�ry jest u�ywany w trakcie startu systemu.

%prep
%setup -q
%patch -p1

%build
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog genromfs.lsm romfs.txt \
	$RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
