from lib.Logger import logger

class ExecCmd:
    def exec_stmt(ssh, cmd):
        logger.info("Preparing to execute command: " + cmd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        
        # 处理错误输出
        for line in stderr:
            logger.error("Error while preparing to execute " + cmd + ": " + line.strip())
            if "error" in line.strip().lower():
                raise Exception("Error in command execution: " + line.strip())

        output_lines = []
        # 处理正常输出
        for line in stdout:
            logger.info("Output from preparing to execute " + cmd + ": " + line.strip())
            output_lines.append(line.strip())

        return "\n".join(output_lines)



ssh_exec = ExecCmd.exec_stmt